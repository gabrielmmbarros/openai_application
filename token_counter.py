# This script calculates and compares token usage and associated costs for different OpenAI models using the same prompt
import tiktoken

model = "gpt-4o-mini"
encoder = tiktoken.encoding_for_model(model)
token_list = encoder.encode("You are a product categorizer.")

print("Token List: ", token_list)
print("Token count: ", len(token_list))
print(f"Cost for the model {model} is ${(len(token_list)/1000) * 0.60}")

model = "o3-mini"
encoder = tiktoken.encoding_for_model(model)
token_list = encoder.encode("You are a product categorizer.")

print("Token List: ", token_list)
print("Token count: ", len(token_list))
print(f"Cost for the model {model} is ${(len(token_list)/1000) * 4.40}")

print(f"The cost of GPT-o3-mini is {round(4.40/0.60, 2)} times higher than GPT-4o-mini")