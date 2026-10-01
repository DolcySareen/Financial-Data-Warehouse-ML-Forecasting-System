import os
from dotenv import load_dotenv

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

print(f"API Key: {FMP_API_KEY}")
print(f"Database URL: {DATABASE_URL}")
