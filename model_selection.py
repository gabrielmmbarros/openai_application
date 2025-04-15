import openai
from dotenv import load_dotenv
import os
import tiktoken

load_dotenv()

openai.api_type = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
openai.api_type = os.getenv("AZURE_OPENAI_API_TYPE")

model = "gpt-4o-mini"

# Initialize the tokenizer for the selected model
encoder = tiktoken.encoding_for_model(model)

# Function to read a file and return its contents
def load_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
            return data
    except IOError as e:
        print(f"Error: {e}")

system_prompt = """
Identify the purchase profile for each customer below.

The output format should be:

customer - describe the customer profile in 3 words

(in english language)
"""

# Load customer purchase data from CSV file
user_prompt = load_file("database\customers_purchase_list.csv")

# Count tokens in the combined prompt to estimate API usage
tokens_list = encoder.encode("Identify" + user_prompt)
token_count = len(tokens_list)
print(f"Number of tokens in input: {token_count}")

# Define model context window and expected response size
expected_input_size = 4096
expected_output_size = 2048

# Switch to a model with larger context window if needed
if token_count >= expected_input_size - expected_output_size:
    model = "gpt-4o"

print(f"Model selected: {model}")

# Prepare the message structure for the OpenAI API call
message_list = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

response = openai.chat.completions.create(
    messages = message_list,
    model = model
)

print(response.choices[0].message.content)