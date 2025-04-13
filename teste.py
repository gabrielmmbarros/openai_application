import openai
from dotenv import load_dotenv
import os

load_dotenv()

# bring the api_key from .env file
openai.api_type = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_type = os.getenv("OPENAI_API_TYPE")

print("Chave obtida do .env:", os.getenv("OPENAI_API_KEY"))