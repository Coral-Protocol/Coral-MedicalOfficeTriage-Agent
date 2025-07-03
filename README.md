# Medical Office Triage Voice Agent

The Medical Office Triage Voice Agent is an intelligent multi-agent voice system that automates patient routing and support in medical office environments. It uses real-time voice processing to understand patient needs and seamlessly transfers them between specialized departments (Triage, Support, and Billing) while maintaining conversation context. The system leverages Deepgram for speech-to-text, Cartesia for text-to-speech, OpenAI for natural language understanding, and LiveKit for real-time communication with noise cancellation capabilities.

## Responsibility
A real-time voice agent for medical offices that automates patient intake, support, and billing routing. **Note:** The prompts in this agent are not for a multi-agent system; it currently works as a standalone agent, does not require interface agents, but will use Coral tools. It is not continuously using the `wait_for_mention` tool to receive commands from other agents.

## Details
- **Framework:** LiveKit Agents
- **Tools Used:** Deepgram STT, Cartesia TTS, OpenAI/Groq LLM, Silero VAD, LiveKit Plugins
- **Date Added:** June 2025
- **License:** MIT
- **Original Source:** [LiveKit Python Agents Examples - Medical Office Triage](https://github.com/livekit-examples/python-agents-examples/tree/main/complex-agents/medical_office_triage)

## Use the Agent

### 1. Clone & Install Dependencies

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. This agent does not require the Interface Agent and is not designed for multi-agent workflows.
<details>

```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/Coral-MedicalOfficeTriage-Agent.git

# Navigate to the project directory:
cd Coral-MedicalOfficeTriage-Agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

### Troubleshooting

If you encounter errors related to post_writer, run these commands:

```bash
# Copy the client sse.py from utils to mcp package (Linux/ Mac)
cp -r utils/sse.py .venv/lib/python3.13/site-packages/mcp/client/sse.py

# OR Copy this for Windows
cp -r utils\sse.py .venv\Lib\site-packages\mcp\client\sse.py
```

</details>

### 2. Configure Environment Variables
<details>

Copy the example file and add your API keys:

```bash
cp .env.example .env
```

Update `.env` with:
- `LIVEKIT_URL` ([Get LiveKit Url](https://cloud.livekit.io/))
- `LIVEKIT_API_KEY` ([Get LiveKit API Key](https://cloud.livekit.io/))
- `LIVEKIT_API_SECRET` ([Get LiveKit API Secret](https://cloud.livekit.io/))
- `DEEPGRAM_API_KEY` ([Get Deepgram API Key](https://deepgram.com/))
- `CARTESIA_API_KEY` ([Get Cartesia API Key](https://cartesia.ai/))
- `API_KEY` ([Get OpenAI API Key](https://platform.openai.com/api-keys)) /([Get GROQ API Key](https://console.groq.com/keys))
- configure the LLM model you want to use
</details>

### 3. Run Agent in Dev Mode
<details>

```bash
uv run triage.py console
```
If you want to run the Agent using [Coral-Studio UI](https://github.com/Coral-Protocol/coral-studio) you can do so but it may not support Voice input and outputs from the UI and only the messages sent using Coral tools will be visible.You
clone it and run it according to the instructions in the readme and run this agent in your terminal.

</details>

## Agent System

- **Triage Agent:** Initial patient intake, determines appropriate department routing
- **Support Agent:** Handles medical services, appointments, and general patient support inquiries
- **Billing Agent:** Manages insurance inquiries, payment questions, and billing support

## Technical Features

- **Multi-Agent Voice System:** Three specialized AI agents working seamlessly together
- **Real-time Voice Processing:** Deepgram speech-to-text, Cartesia text-to-speech, OpenAI language understanding
- **Intelligent Routing:** Automatic patient transfer between departments based on conversation analysis

## Usage Examples
<details>

1. **Start the application using the console command** - The system initializes with all three agents ready
2. **Begin speaking when you hear the system is ready** - You'll be connected to the Triage Agent first
3. **Triage Agent interaction** - The Triage Agent will:
   - Listen to your initial request or concern
   - Ask clarifying questions about your medical office needs
   - Determine whether you need appointment scheduling, medical support, or billing assistance
   - Route you to the appropriate specialist agent based on your needs
4. **Automatic transfer to specialist agents**:
   - **Support Agent** - If you need:
     - Medical appointment scheduling
     - General patient support inquiries
     - Information about medical services
     - Health-related questions and guidance
   - **Billing Agent** - If you need:
     - Insurance verification and claims
     - Payment processing and billing questions
     - Cost estimates for procedures
     - Financial assistance programs
5. **Continue the conversation naturally** - Once transferred:
   - The specialist agent has full context of your previous conversation
   - You can ask follow-up questions specific to that department
   - The agent can transfer you back to Triage or to another specialist if needed
   - All conversation history is preserved throughout transfers

</details>

## Creator Details
- **Name:** Ahsen Tahir
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

