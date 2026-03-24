# 🚀 FinAssist

**FinAssist** is a full-stack, AI-powered personal financial assistant designed with multi-agent intelligence, semantic expense understanding, and a premium interactive dashboard. Built for the ET Hackathon.

## ✨ Features
- **Multi-Agent Core**: Dedicated LLM agents for Expense Classification, Tax deduction mapping, and Financial Trend Analysis.
- **RAG-Powered Tax Intelligence**: Utilizes FAISS local vector databases to read tax rule logic and deduce category rules on the fly.
- **Micro-Animated Premium UI**: A highly polished, glassmorphism dashboard built with Vite, React, Recharts, and Vanilla CSS.
- **Conversational AI**: Interact dynamically with your transaction history through a built-in AI chat module.

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy (SQLite/PostgreSQL adaptable), OpenAI APIs, FAISS 
- **Frontend:** React, Vite, Lucide Icons, Recharts
- **Data Ecosystem:** Pandas, Numpy, Statsmodels 

## ⚙️ How to Setup & Run

### Method 1: The Easy Way (Windows)
We've included a convenient PowerShell script that instantly launches both the Backend API and the Frontend React Server concurrently.
1. Open your terminal in the root directory.
2. Execute the script:
   ```powershell
   .\run.ps1
   ```
3. Open `http://localhost:5173` to view your Dashboard!

### Method 2: Manual Setup
**1. Backend:**
```bash
cd FinAssist/backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
> **Important:** Set an `OPENAI_API_KEY` in `FinAssist/backend/.env` to experience the full AI conversational and classification engine. If no key is present, the app safely overrides to mock data for a seamless demonstration.

**2. Frontend:**
```bash
cd FinAssist/frontend
npm install
npm run dev
```

---
*Developed for the ET Hackathon.* 🌟
