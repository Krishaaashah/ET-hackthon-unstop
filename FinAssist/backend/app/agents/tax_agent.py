import json
from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.services.rag_service import rag_service

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

def analyze_tax_deductibility(merchant: str, description: str, category: str) -> dict:
    """Determines if an expense is likely tax deductible based on the knowledge base."""
    # Step 1: Query RAG for relevant tax rules
    rag_results = rag_service.search(f"{merchant} {description} {category}", k=2)
    kb_context = "\n".join([res["document"] for res in rag_results])
    
    if not client:
        return {"is_tax_deductible": False, "tax_category": None, "reasoning": "Mock"}
        
    prompt = f"""
    You are an AI Tax Advisor.
    Transaction:
    Merchant: {merchant}
    Description: {description}
    Category: {category}
    
    Knowledge Base excerpts:
    {kb_context}
    
    Determine if this transaction is likely tax-deductible.
    Return only valid JSON format:
    {{"is_tax_deductible": true/false, "tax_category": "section/category", "reasoning": "text"}}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"is_tax_deductible": False, "tax_category": None, "reasoning": str(e)}
