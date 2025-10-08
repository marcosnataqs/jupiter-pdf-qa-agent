# 🪐 Project Jupiter — PDF QA Agent

## 🎯 Overview

This is a **30-minute live coding challenge** where you'll implement:

- ✅ **PDF Ingestion**: Extract text, chunk, and store in memory
- ✅ **Retrieval Tool**: Return top-k relevant chunks with citations
- ✅ **Conversation Memory**: Maintain context for follow-ups
- ✅ **Multi-Turn Chat**: Ask questions and receive grounded answers

## 🏗️ What's Provided (Minimal Scaffold)

```
├── src/
│   ├── agent.py       # ✅ LangGraph ReAct agent (complete)
│   └── tools.py       # ⚠️  Placeholder retrieval tool (TODO)
├── app.py             # ✅ Streamlit UI with chat + file upload
├── requirements.txt   # ✅ Dependencies configured
└── README.md          # 📖 This file
```

### What Works Out of the Box

- **Streamlit UI**: Chat interface with file uploader
- **LangGraph Agent**: Complete ReAct agent with tool calling setup
- **Tool Registry**: Placeholder tool ready to be implemented

## 📋 Prerequisites

- Python 3.11 or higher
- OpenAI API key

## 🚀 Quick Start

### 1. Setup

```bash
# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=sk-your-key-here" > .env

# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies (includes Streamlit and all required packages)
pip install -r requirements.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

### 3. Open in Browser

Navigate to `http://localhost:8501`

Streamlit will automatically open your browser. If it doesn't, manually open the URL shown in your terminal.

### 4. Start Coding!