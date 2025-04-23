import openai
from dotenv import load_dotenv
import os

# This function loads environment variables from .env file into the application's environment,
# allowing for secure management of sensitive data
load_dotenv()

# Configure the OpenAI API with Azure credentials from environment variables
openai.api_type = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
openai.api_type = os.getenv("AZURE_OPENAI_API_TYPE")

model = "gpt-4o"

# Function to load file contents
def load_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
            return data
    except IOError as e:
        print(f"Error: {e}")


# Function to save analysis results to a file
def save_review(file_name, content):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error saving file: {e}")

import os

# Function that extracts product names from filenames
def get_product_names():
    # Get the list of files in the directory
    reviews_folder = "./database/customers_reviews"
    files = os.listdir(reviews_folder)
    
    product_names = []
    for file in files:
        if file.startswith("review-") and file.endswith(".txt"):
            
            product_name = file[7:-4]  # Remove 'review-' (7 characters) and '.txt' (4 characters)
            product_names.append(product_name)
    
    return product_names

# Get the product names
products = get_product_names()
print(products)


def sentiment_analyzer(product):
    """
    Analyzes sentiment of product reviews using AI
    """
    system_prompt = f"""
        You are a sentiment analyzer for product reviews.
        Write a paragraph with up to 50 words summarizing the reviews and 
        then assign an overall sentiment for the product.
        Also identify 3 strengths and 3 weaknesses identified from the reviews.

        # Output Format

        Product Name:
        Review Summary:
        Overall Sentiment: [use only Positive, Negative or Neutral here]
        Strengths: list with three bullets
        Weaknesses: list with three bullets
    """

    # Load product review from file
    user_prompt = load_file(f"./database/customers_reviews/review-{product}.txt")
    print(f"Started sentiment analysis for product {product}")

    # Make API call to OpenAI for sentiment analysis
    response = openai.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            },
        ],
        model = model,
    )

    # Extract and save the analysis results
    response_text = response.choices[0].message.content
    save_review(f"./database/review_analysis/review-{product}-analyzed.txt", response_text)


# Run the sentiment analysis function
#sentiment_analyzer("mineral_makeup")

product_name_list = get_product_names()
for product in product_name_list:
    sentiment_analyzer(product)

