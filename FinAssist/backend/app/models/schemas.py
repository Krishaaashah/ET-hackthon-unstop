from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from app.models.database import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    amount = Column(Float, nullable=False)
    merchant = Column(String, index=True)
    description = Column(String)
    
    # AI Classified fields
    category = Column(String, index=True, nullable=True) 
    confidence_score = Column(Float, nullable=True)
    
    # Tax Insights fields
    is_tax_deductible = Column(Boolean, default=False)
    tax_category = Column(String, nullable=True)

class UserFeedback(Base):
    __tablename__ = "user_feedback"
    
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, index=True)
    corrected_category = Column(String)
    corrected_tax_status = Column(Boolean)
