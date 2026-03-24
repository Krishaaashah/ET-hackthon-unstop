import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# We expect OPENAI_API_KEY to be provided in the environment or .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Using SQLite for the prototype as requested
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./finassist.db")
