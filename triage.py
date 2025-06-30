import logging
import urllib.parse
from dataclasses import dataclass, field
from typing import Optional

from dotenv import load_dotenv
import os
from livekit.agents import JobContext, WorkerOptions, cli, mcp
from livekit.agents.llm import function_tool
from livekit.agents.voice import Agent, AgentSession, RunContext
from livekit.plugins import cartesia, deepgram, openai, silero, groq
from livekit.plugins import noise_cancellation

from utils import load_prompt

logger = logging.getLogger("medical-office-triage")
logger.setLevel(logging.INFO)

load_dotenv()

def get_llm_instance():
    """Get LLM instance based on environment configuration"""
    llm_provider = os.getenv("LLM_PROVIDER", "openai").lower()
    llm_model = os.getenv("LLM_MODEL", "gpt-4o-mini")
    api_key = os.getenv("API_KEY")
    
    if llm_provider == "openai":
        return openai.LLM(model=llm_model, api_key=api_key)
    elif llm_provider == "groq":
        return groq.LLM(model=llm_model, api_key=api_key)
    else:
        # Add more providers as needed
        logger.warning(f"Unsupported LLM provider: {llm_provider}. Falling back to OpenAI.")
        return openai.LLM(model=llm_model, api_key=api_key)

@dataclass
class UserData:
    """Stores data and agents to be shared across the session"""
    personas: dict[str, Agent] = field(default_factory=dict)
    prev_agent: Optional[Agent] = None
    ctx: Optional[JobContext] = None

    def summarize(self) -> str:
        return "User data: Medical office triage system"

RunContext_T = RunContext[UserData]

class BaseAgent(Agent):
    async def on_enter(self) -> None:
        agent_name = self.__class__.__name__
        logger.info(f"Entering {agent_name}")

        userdata: UserData = self.session.userdata
        if userdata.ctx and userdata.ctx.room:
            await userdata.ctx.room.local_participant.set_attributes({"agent": agent_name})

        chat_ctx = self.chat_ctx.copy()

        if userdata.prev_agent:
            items_copy = self._truncate_chat_ctx(
                userdata.prev_agent.chat_ctx.items, keep_function_call=True
            )
            existing_ids = {item.id for item in chat_ctx.items}
            items_copy = [item for item in items_copy if item.id not in existing_ids]
            chat_ctx.items.extend(items_copy)

        chat_ctx.add_message(
            role="system",
            content=f"You are the {agent_name}. {userdata.summarize()}"
        )
        await self.update_chat_ctx(chat_ctx)
        self.session.generate_reply()

    def _truncate_chat_ctx(
        self,
        items: list,
        keep_last_n_messages: int = 6,
        keep_system_message: bool = False,
        keep_function_call: bool = False,
    ) -> list:
        """Truncate the chat context to keep the last n messages."""
        def _valid_item(item) -> bool:
            if not keep_system_message and item.type == "message" and item.role == "system":
                return False
            if not keep_function_call and item.type in ["function_call", "function_call_output"]:
                return False
            return True

        new_items = []
        for item in reversed(items):
            if _valid_item(item):
                new_items.append(item)
            if len(new_items) >= keep_last_n_messages:
                break
        new_items = new_items[::-1]

        while new_items and new_items[0].type in ["function_call", "function_call_output"]:
            new_items.pop(0)

        return new_items

    async def _transfer_to_agent(self, name: str, context: RunContext_T) -> Agent:
        """Transfer to another agent while preserving context"""
        userdata = context.userdata
        current_agent = context.session.current_agent
        next_agent = userdata.personas[name]
        userdata.prev_agent = current_agent

        return next_agent


class TriageAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(
            instructions=load_prompt('triage_prompt.yaml'),
            stt=deepgram.STT(),
            llm=get_llm_instance(),
            tts=cartesia.TTS(),
            vad=silero.VAD.load()
        )

    @function_tool
    async def transfer_to_support(self, context: RunContext_T) -> Agent:
        await self.session.say("I'll transfer you to our Patient Support team who can help with your medical services request.")
        return await self._transfer_to_agent("support", context)

    @function_tool
    async def transfer_to_billing(self, context: RunContext_T) -> Agent:
        await self.session.say("I'll transfer you to our Medical Billing department who can assist with your insurance and payment questions.")
        return await self._transfer_to_agent("billing", context)


class SupportAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(
            instructions=load_prompt('support_prompt.yaml'),
            stt=deepgram.STT(),
            llm=get_llm_instance(),
            tts=cartesia.TTS(),
            vad=silero.VAD.load()
        )

    @function_tool
    async def transfer_to_triage(self, context: RunContext_T) -> Agent:
        await self.session.say("I'll transfer you back to our Medical Office Triage agent who can better direct your inquiry.")
        return await self._transfer_to_agent("triage", context)

    @function_tool
    async def transfer_to_billing(self, context: RunContext_T) -> Agent:
        await self.session.say("I'll transfer you to our Medical Billing department for assistance with your insurance and payment questions.")
        return await self._transfer_to_agent("billing", context)


class BillingAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(
            instructions=load_prompt('billing_prompt.yaml'),
            stt=deepgram.STT(),
            llm=get_llm_instance(),
            tts=cartesia.TTS(),
            vad=silero.VAD.load()
        )

    @function_tool
    async def transfer_to_triage(self, context: RunContext_T) -> Agent:
        await self.session.say("I'll transfer you back to our Medical Office Triage agent who can better direct your inquiry.")
        return await self._transfer_to_agent("triage", context)

    @function_tool
    async def transfer_to_support(self, context: RunContext_T) -> Agent:
        await self.session.say("I'll transfer you to our Patient Support team who can help with your medical services request.")
        return await self._transfer_to_agent("support", context)


async def entrypoint(ctx: JobContext):
    await ctx.connect()

    # MCP Server configuration
    base_url = os.getenv("CORAL_SSE_URL")
    params = {
       # "waitForAgents": 1,
        "agentId": os.getenv("CORAL_AGENT_ID"),
        "agentDescription": "You are a helpful medical office triage assistant that can help patients with appointments, billing questions, and general support."
    }
    query_string = urllib.parse.urlencode(params)
    MCP_SERVER_URL = f"{base_url}?{query_string}"

    userdata = UserData(ctx=ctx)
    triage_agent = TriageAgent()
    support_agent = SupportAgent()
    billing_agent = BillingAgent()

    # Register all agents in the userdata
    userdata.personas.update({
        "triage": triage_agent,
        "support": support_agent,
        "billing": billing_agent
    })

    session = AgentSession[UserData](
        userdata=userdata,
        mcp_servers=[
            mcp.MCPServerHTTP(
                url=MCP_SERVER_URL,
                timeout=10,
                client_session_timeout_seconds=10,
            ),
        ]
    )

    await session.start(
        agent=triage_agent,  # Start with the Medical Office Triage agent
        room=ctx.room,
    )

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
