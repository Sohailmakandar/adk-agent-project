# 🤖 Smart Research Assistant Agent
### Google Skills Lab — Track 3: Engineer AI Agents with ADK

[![Google ADK](https://img.shields.io/badge/Google%20ADK-Agent%20Development%20Kit-blue)](https://google.github.io/adk-docs/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Model-Gemini%202.0%20Flash-orange)](https://deepmind.google/technologies/gemini/)

---

## 📌 Overview

The **Smart Research Assistant Agent** is an AI-powered agent built using **Google's Agent Development Kit (ADK)**. It demonstrates core ADK concepts including multi-tool orchestration, session management, and Gemini model integration.

### 🎯 What It Can Do

| Capability | Tool Used |
|---|---|
| 🔍 Research any topic | `search_topic` |
| 📝 Summarize long text | `summarize_text` |
| 💾 Save & retrieve notes | `save_note`, `list_notes` |
| 🧮 Calculate math expressions | `calculate` |
| 🌤️ Get weather information | `weather_info` |
| 🕐 Get current date & time | `get_current_time` |

---

## 🏗️ Project Structure

```
adk-agent-project/
│
├── agent.py          # Root agent definition (ADK Agent)
├── tools.py          # All custom tools decorated with @tool
├── main.py           # Entry point — interactive & demo modes
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variable template
└── README.md         # This file
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/adk-agent-project.git
cd adk-agent-project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
# Get your key at: https://aistudio.google.com/apikey
```

---

## 🚀 Running the Agent

### Interactive Mode (Chat with the agent)
```bash
python main.py
```

### Demo Mode (See all features automatically)
```bash
python main.py --demo
```

### Using ADK Web UI
```bash
adk web
```
Then open `http://localhost:8000` in your browser.

---

## 💬 Example Interactions

```
🙋 You: Research the topic: machine learning
🤖 Agent: Here's what I found about machine learning...

🙋 You: Calculate sqrt(256) + 100
🤖 Agent: sqrt(256) + 100 = 116.0

🙋 You: What's the weather in Bangalore?
🤖 Agent: Current weather in Bangalore: 28°C, Partly Cloudy...

🙋 You: Save a note titled "ML Notes" with content: ML is a subset of AI.
🤖 Agent: Note saved successfully! Note ID: 1

🙋 You: List all my notes
🤖 Agent: You have 1 saved note: "ML Notes"...
```

---

## 🧠 Key ADK Concepts Demonstrated

- **`Agent`** — Core agent with name, model, instructions, and tools
- **`@tool`** — Decorator to register Python functions as agent tools
- **`Runner`** — Orchestrates agent execution and event streaming
- **`InMemorySessionService`** — Manages conversation sessions
- **Multi-turn conversations** — Agent remembers context within a session

---

## 📚 References

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google AI Studio](https://aistudio.google.com/)
- [ADK GitHub Repository](https://github.com/google/adk-python)
- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)

---

## 👤 Author

**Sohail** — MCA Student, Jain (Deemed-to-be University)  
Submitted for: Google Skills Lab — Track 3 (Engineer AI Agents with ADK)
