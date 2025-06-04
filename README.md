# Medical Voice Agents with Deepgram

A sophisticated medical office triage system powered by voice AI agents that can intelligently route patients to appropriate departments through natural conversation.

## 🎯 Functionality

This application provides an intelligent medical office triage system featuring:

- **Multi-Agent Voice System**: Three specialized AI agents (Triage, Support, and Billing) that work together seamlessly
- **Real-time Voice Processing**: Uses Deepgram for speech-to-text, Cartesia for text-to-speech, and OpenAI for natural language understanding
- **Intelligent Routing**: Automatically transfers patients between departments based on their needs

### Agent Capabilities:

- **Triage Agent**: Initial patient intake, determines appropriate department
- **Support Agent**: Handles medical services, appointments, and general patient support
- **Billing Agent**: Manages insurance inquiries, payment questions, and billing support

## 🚀 Setup Instructions

### 1. Environment Configuration

First, copy the example environment file and add your API keys:

```bash
cp env.example .env
```

Edit the `.env` file and add your API keys:
- LiveKit API key and secret (get from [LiveKit Console](https://console.livekit.io))
- OpenAI API key (get from [OpenAI Console](https://platform.openai.com))
- Deepgram API key (get from [Deepgram Console](https://console.deepgram.com))
- Cartesia API key (get from [Cartesia Console](https://cartesia.ai))

### 2. Install Dependencies

Install UV package manager:

```bash
pip install uv
```

Sync project dependencies:

```bash
uv sync
```

### 3. Run the Application

Start the medical triage console:

```bash
uv run triage.py console
```

The system will start with the Triage Agent and wait for voice input. Speak naturally to interact with the medical office system.

## 🔧 Technical Stack

- **Python 3.13+**: Modern Python with type hints
- **LiveKit Agents**: Real-time voice agent framework
- **OpenAI GPT-4o-mini**: Language understanding and generation
- **Deepgram**: Speech-to-text processing
- **Cartesia**: High-quality text-to-speech
- **Silero VAD**: Voice activity detection
- **UV**: Fast Python package manager

## 📁 Project Structure

```
medical_voice_agents_deepgram/
├── triage.py              # Main application with agent definitions
├── utils.py               # Utility functions for prompt loading
├── prompts/               # YAML prompt configurations for each agent
│   ├── triage_prompt.yaml
│   ├── support_prompt.yaml
│   └── billing_prompt.yaml
├── pyproject.toml         # Project configuration and dependencies
├── .env                   # Environment variables (create from env.example)
└── README.md              # This file
```

