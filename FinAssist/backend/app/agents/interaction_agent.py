from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

def handle_user_query(query: str, context: str) -> str:
    """Conversational AI to answer finance questions based on context."""
    if not client:
        return "I am unable to connect to the AI service."

    prompt = f"""
    You are FinAssist, a helpful personal financial assistant.
    User Query: {query}
    Current Financial Context:
    {context}
    
    Provide a brief, helpful answer.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)
