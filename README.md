# 🤖 AI Agent Crew

A multi-agent AI system built with **CrewAI** and **Streamlit** that researches, analyzes, and writes professional reports on any topic using a collaborative agent pipeline.

## Architecture

```
User Input (topic)
    │
    ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  🔍 Researcher │ ──▶ │  📊 Analyst   │ ──▶ │  ✍️ Writer    │
│  (Data Gather) │     │  (Insights)   │     │  (Report)     │
└──────────────┘     └──────────────┘     └──────────────┘
                                                  │
                                                  ▼
                                          Final Report
```

**Sequential Pipeline:**
1. **Researcher Agent** — Gathers comprehensive data and facts on the topic
2. **Analyst Agent** — Analyzes findings and extracts key insights/trends
3. **Writer Agent** — Transforms insights into a structured, engaging report

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | [CrewAI](https://crewai.com) |
| LLM Backend | OpenRouter (Llama 4 Maverick) |
| Frontend | Streamlit |
| Language | Python 3.11+ |

## Quick Start

### 1. Clone & Setup

```bash
git clone <repo-url>
cd ai-agent
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file with your API credentials:

```env
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL_NAME=openrouter/meta-llama/llama-4-maverick:free
OPENROUTER_API_KEY=your-api-key-here
```

### 4. Run the App

**Streamlit UI:**
```bash
streamlit run app.py
```

**CLI mode:**
```bash
python crew.py
```

## Project Structure

```
ai-agent/
├── app.py              # Streamlit frontend
├── agents.py           # Agent definitions (Researcher, Analyst, Writer)
├── tasks.py            # Task definitions for each agent
├── crew.py             # Crew orchestration & execution
├── tools.py            # Custom tools (file I/O, directory listing)
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## License

MIT
