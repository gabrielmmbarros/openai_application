import openai
from dotenv import load_dotenv
import os

load_dotenv()

# bring the api_key from .env file
openai.api_type = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
openai.api_type = os.getenv("AZURE_OPENAI_API_TYPE")

# 'completion' is the feature that allows chatting (user prompt <-> system response)
response = openai.chat.completions.create(
    messages = [
        {
            "role": "system",
            "content": "List the most popular products in web sales. List only names, no description."
        },
        {
            "role": "user",
            "content": "List 3 sustainable products."
        },
    ],
    model = "gpt-4o"
)

print(response.choices[0].message.content)