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

1. Start the application using the console command
2. Begin speaking when you hear the system is ready
3. The Triage Agent will listen and determine your needs
4. You'll be automatically transferred to the appropriate specialist agent
5. Continue the conversation naturally - context is preserved across transfers

## Creator Details

**Name:** Ahsen Tahir 
**Affiliation:** LiveKit 
**Original Source:** [LiveKit Examples Repository](https://github.com/livekit-examples/python-agents-examples/tree/main/complex-agents/medical_office_triage)  
**Contact:** ahsen.t@coralprotocol.org

