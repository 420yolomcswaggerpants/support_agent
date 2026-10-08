# AI Customer Support Agent

A rule-based customer support chatbot for Nimbus Coffee Roasters, built with DeepSeek and Streamlit.

## Live Demo
https://support-agent-420yolomcswaggerpants.streamlit.app

## What It Does
- Acts as a customer support agent for a fictional coffee company
- Follows strict rules defined in the system prompt
- Answers FAQs from a local document
- Remembers conversation context
- Includes quick-reply FAQ buttons

## Features
- System prompt defines the agent's personality and rules
- Reads FAQ data from a text file
- Refuses to answer off-topic questions
- Memory via Streamlit session state
- Clean chat interface

## Tech Stack
- Python
- Streamlit
- DeepSeek API
- OpenAI Python SDK

## How It Works
1. The system prompt defines the agent's identity and rules
2. FAQ data is loaded from `faq.txt`
3. User asks a question or clicks a quick-reply button
4. The app sends conversation history + FAQ to DeepSeek
5. The agent responds according to its rules

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your DeepSeek API key to `.streamlit/secrets.toml`
4. Run: `streamlit run app.py`

## Skills Demonstrated
- Prompt engineering
- Rule-based AI agents
- Session state management
- File handling
- Deployment
