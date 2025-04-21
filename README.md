Agentic AI Customer Support Chatbot

An intelligent, semi-guided Agentic AI chatbot built to serve as a customer support assistant for an e-commerce platform. It uses LangGraph for multi-step reasoning and runs a local Mistral LLM via Ollama, with a responsive React + Tailwind frontend and a FastAPI backend in Python.
Features

  - Agentic AI: Multi-step decision-making using LangGraph.

  - Local LLM (Mistral via Ollama): Fully offline-capable, no external APIs.

  - React Frontend: Fast, clean, and user-friendly with Vite + Tailwind CSS.

  - FastAPI Backend: Lightweight and efficient REST API in Python.

  - Modular Setup: Easy to customize, expand, and plug in new tools or logic.

 
Setup Instructions (Windows - CMD Friendly)

1. Clone the Repo

git clone https://github.com/yourusername/agentic-ai-chatbot.git
cd agentic-ai-chatbot

2. Install and Run Ollama

Make sure you’ve installed Ollama on your system.

ollama pull mistral
ollama run mistral

3. Set Up the Backend

Ensure Python and pip are available in CMD.

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

FastAPI server runs on http://localhost:8000

4. Set Up the Frontend

Ensure Node.js and npm are installed.

cd frontend
npm install
npm run dev

Frontend runs on http://localhost:5173

Use Cases

  - Answering e-commerce customer questions

  - Order tracking and returns

  - Product information and FAQs

  - Intelligent support agent simulation

Roadmap

- Add persistent memory

- Add multi-agent capability

- Add user authentication

- Docker support

Built With

LangGraph – Agentic workflows

Ollama + Mistral – Local language model

FastAPI – Python backend API

React + Vite – Modern frontend framework

Tailwind CSS – Utility-first CSS styling


Contributing

PRs and feedback are welcome. Fork it, improve it, and feel free to share your customizations.

License

MIT License – Free to use, improve, and share.

Author

Built by Ashik — passionate about Agentic AI, clean interfaces, and building useful tools that work offline.
