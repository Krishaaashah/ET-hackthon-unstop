import pandas as pd
from typing import List
from app.schemas.transaction import TransactionCreate

def parse_csv_transactions(file_path: str) -> List[TransactionCreate]:
    """
    Parses a CSV file containing transactions and normalizes them into TransactionCreate schemas.
    Expected columns: date, description, amount
    """
    try:
        df = pd.read_csv(file_path)
        # Normalize columns
        df.columns = [str(col).strip().lower() for col in df.columns]
        
        transactions = []
        for _, row in df.iterrows():
            # Basic mapping logic - adjust based on actual CSV format
            amount = float(row.get('amount', 0))
            if amount < 0:
                amount = abs(amount)  # Store expenses as positive absolute values for simplicity
                
            desc = str(row.get('description', 'Unknown')).strip()
            
            transaction = TransactionCreate(
                amount=amount,
                merchant=desc,
                description=desc,
                date=pd.to_datetime(row.get('date', pd.Timestamp.now()))
            )
            transactions.append(transaction)
            
        return transactions
    except Exception as e:
        print(f"Error parsing CSV: {e}")
        return []
