import openai
from dotenv import load_dotenv
import os

# This function loads environment variables from .env file into the application's environment,
# allowing for secure management of sensitive data
load_dotenv()

# bring the api_key from .env file
openai.api_type = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
openai.api_type = os.getenv("AZURE_OPENAI_API_TYPE")

model = "gpt-4o"

# this function categorizes a given product name into one of the provided categories
def categorize_product(product_name, product_categories_list):
    system_prompt = f"""
            You are a product categorizer.
            You must assume the categories present in the list below.

            # List of Valid Categories
            {product_categories_list.split(",")}

            # Output Format
            Product: Product Name
            Category: present the product's category

            # Example Output
            Product: Solar rechargeable electric toothbrush
            Category: Green Electronics
        """

    # 'completion' is the feature that allows chatting (user prompt  <-> system response)
    response = openai.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": product_name

            },
        ],
        model = model,
        temperature = 0,
        max_tokens = 200

    )

    return response.choices[0].message.content

# the user must type a list of product categories
categories_list = input("List the valid categories, separated by commas: ")

while True:
    product_name = input("Provide a product name: ")
    response_text = categorize_product(product_name, categories_list)
    print(response_text)

