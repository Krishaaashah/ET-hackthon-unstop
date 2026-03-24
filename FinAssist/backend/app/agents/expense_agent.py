import json
from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

def classify_expense(merchant: str, description: str, amount: float) -> dict:
    """Classifies an expense into a category using LLM context if available."""
    if not client:
        return {"category": "Miscellaneous", "confidence_score": 0.5, "reasoning": "Mock API"}
        
    prompt = f"""
    You are an AI Expense Classifier.
    Given a transaction:
    Merchant: {merchant}
    Description: {description}
    Amount: {amount}
    
    Categorize this transaction into a standard budget category (e.g. Food, Travel, Rent, Software, Utilities).
    Provide a confidence score (0.0 to 1.0) and a brief reasoning in exactly the following JSON format:
    {{"category": "category_name", "confidence_score": 0.9, "reasoning": "reasoning text"}}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error classifying expense: {e}")
        return {"category": "Unknown", "confidence_score": 0.0, "reasoning": str(e)}
