#  FinAssist

**FinAssist** is a full-stack, AI-powered personal financial assistant designed with multi-agent intelligence, semantic expense understanding, and a premium interactive dashboard. Built for the ET Hackathon.

##  Features
- **Multi-Agent Core**: Dedicated LLM agents for Expense Classification, Tax deduction mapping, and Financial Trend Analysis.
- **RAG-Powered Tax Intelligence**: Utilizes FAISS local vector databases to read tax rule logic and deduce category rules on the fly.
- **Micro-Animated Premium UI**: A highly polished, glassmorphism dashboard built with Vite, React, Recharts, and Vanilla CSS.
- **Conversational AI**: Interact dynamically with your transaction history through a built-in AI chat module.

## workflow of system

https://github.com/user-attachments/assets/b299d077-05b3-479a-b563-06e602d03a12




##  Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy (SQLite/PostgreSQL adaptable), OpenAI APIs, FAISS 
- **Frontend:** React, Vite, Lucide Icons, Recharts
- **Data Ecosystem:** Pandas, Numpy, Statsmodels 

##  How to Setup & Run

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
copy .env.example .env
uvicorn app.main:app --reload --port 8000
```
> **Important:** Set an `OPENAI_API_KEY` in `FinAssist/backend/.env` to experience the full AI conversational and classification engine. If no key is present, the app safely overrides to mock data for a seamless demonstration.

LLM provider switch in backend `.env`:
- `LLM_PROVIDER=openai` (default)
- `LLM_PROVIDER=gemini`
- Then set matching provider key (`OPENAI_API_KEY` or `GEMINI_API_KEY`).

Backend `.env` now includes sections for:
- Core app settings (`DATABASE_URL`, `WEBHOOK_SECRET`, `REPORT_LOOKBACK_DAYS`)
- OpenAI (`OPENAI_API_KEY`)
- SMS providers (Twilio / MSG91 / Fast2SMS)
- Payment gateways (Razorpay / Stripe)
- Account Aggregator/FIU placeholders
- Dev bootstrap control (`AUTO_CREATE_TABLES=true|false`)
- Logging control (`LOG_LEVEL`)
- Rate-limit backend (`RATE_LIMIT_BACKEND=memory|redis`, optional `REDIS_URL`)
- CORS + host hardening (`CORS_ALLOWED_ORIGINS`, `CORS_ALLOW_CREDENTIALS`, `TRUSTED_HOSTS`)
- Security headers + HTTPS HSTS toggle (`SECURITY_HEADERS_ENABLED`, `REQUIRE_HTTPS`)
- Auto-classification feature flag (`AUTO_CLASSIFICATION_ENABLED`)
- LangGraph checkpoint path (`LANGGRAPH_CHECKPOINT_PATH`)

Operational health endpoints:
- Liveness: `GET /health`
- Readiness: `GET /health/ready` (database + RAG index checks)

**2. Frontend:**
```bash
cd FinAssist/frontend
npm install
copy .env.example .env
npm run dev
```

Frontend `.env` uses:
- `VITE_API_BASE_URL` (default: `http://localhost:8000/api`)

### Backend Tests
```bash
cd FinAssist/backend
python -m pytest -q
```

### Database Migrations (Alembic)
```bash
cd FinAssist/backend
alembic upgrade head
```

Notes:
- Use `AUTO_CREATE_TABLES=true` for local quick-start.
- Use `AUTO_CREATE_TABLES=false` in production and rely on Alembic migrations.

### CI Pipeline
- GitHub Actions workflow: `FinAssist/.github/workflows/ci.yml`
- Runs backend migrations + tests (`alembic upgrade head`, `python -m pytest -q`) and frontend lint/build (`npm run lint -- --max-warnings=0`, `npm run build`) on push/PR.

### Production Preflight and Cutover
Use this before production deployment to catch unsafe config values.

```bash
cd FinAssist/backend
python scripts/production_preflight.py --strict
```

Production environment template:
- `FinAssist/backend/.env.production.example`

Recommended cutover order:
1. Fill production env vars from `FinAssist/backend/.env.production.example`.
2. Run preflight check in strict mode.
3. Run migrations: `alembic upgrade head`.
4. Start backend and verify:
   - `GET /health`
   - `GET /health/ready`
5. Validate feature metrics endpoint after smoke traffic:
   - `GET /api/realtime/metrics/feedback`

---
*Developed for the ET Hackathon.* 🌟
