from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os

from app.models.database import get_db
from app.models.schemas import Transaction
from app.schemas.transaction import TransactionResponse
from app.services.ingestion_service import parse_csv_transactions
from app.agents.expense_agent import classify_expense
from app.agents.tax_agent import analyze_tax_deductibility

router = APIRouter()

@router.post("/upload", response_model=List[TransactionResponse])
async def upload_transactions(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
        
    parsed_transactions = parse_csv_transactions(file_location)
    os.remove(file_location)
    
    saved_transactions = []
    
    for p_txn in parsed_transactions:
        expense_info = classify_expense(p_txn.merchant, p_txn.description, p_txn.amount)
        category = expense_info.get("category", "Unknown")
        conf = expense_info.get("confidence_score", 0.0)
        
        tax_info = analyze_tax_deductibility(p_txn.merchant, p_txn.description, category)
        
        db_txn = Transaction(
            date=p_txn.date,
            amount=p_txn.amount,
            merchant=p_txn.merchant,
            description=p_txn.description,
            category=category,
            confidence_score=conf,
            is_tax_deductible=tax_info.get("is_tax_deductible", False),
            tax_category=tax_info.get("tax_category", None)
        )
        db.add(db_txn)
        db.commit()
        db.refresh(db_txn)
        saved_transactions.append(db_txn)
        
    return saved_transactions

@router.get("/", response_model=List[TransactionResponse])
def get_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Transaction).offset(skip).limit(limit).all()
