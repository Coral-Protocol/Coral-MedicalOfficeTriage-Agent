# Medical Office Triage Voice Agent

**Responsibility:** The Medical Office Triage Voice Agent is an intelligent multi-agent voice system that automates patient routing and support in medical office environments. It uses real-time voice processing to understand patient needs and seamlessly transfers them between specialized departments (Triage, Support, and Billing) while maintaining conversation context. The system leverages Deepgram for speech-to-text, Cartesia for text-to-speech, OpenAI for natural language understanding, and LiveKit for real-time communication with noise cancellation capabilities.

## Details

**Framework:** LiveKit Agents  
**Tools used:** Deepgram STT, Cartesia TTS, OpenAI LLM, Silero VAD, LiveKit Plugins  
**AI model:** GPT-4o-mini  
**Date added:** June 2025  
**License:** MIT  
**Original source:** [LiveKit Python Agents Examples - Medical Office Triage](https://github.com/livekit-examples/python-agents-examples/tree/main/complex-agents/medical_office_triage)

## Install Dependencies:

```bash
pip install uv
uv sync
```

## Configure Environment Variables:

```bash
# Copy example environment file
cp env.example .env
```

Edit the `.env` file and add your API keys:
- LiveKit API key and secret (get from [LiveKit Console](https://console.livekit.io))
- OpenAI API key (get from [OpenAI Console](https://platform.openai.com))
- Deepgram API key (get from [Deepgram Console](https://console.deepgram.com))
- Cartesia API key (get from [Cartesia Console](https://cartesia.ai))

## Run agent command:

```bash
uv run triage.py console
```

## Agent Capabilities:

- **Triage Agent**: Initial patient intake, determines appropriate department routing
- **Support Agent**: Handles medical services, appointments, and general patient support inquiries
- **Billing Agent**: Manages insurance inquiries, payment questions, and billing support

## Technical Features:

- **Multi-Agent Voice System**: Three specialized AI agents working seamlessly together
- **Real-time Voice Processing**: Deepgram speech-to-text, Cartesia text-to-speech, OpenAI language understanding
- **Intelligent Routing**: Automatic patient transfer between departments based on conversation analysis

## Example Usage:

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

## Creator Details

**Name:** Ahsen Tahir 

**Contact:** ahsen.t@coralprotocol.org

