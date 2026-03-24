from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import transactions
from app.models.database import engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FinAssist API",
    description="Backend for the AI-powered personal financial assistant.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for hackathon development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transactions.router, prefix="/api/transactions", tags=["Transactions"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FinAssist API!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
