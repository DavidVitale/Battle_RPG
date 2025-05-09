import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("XAI_API_KEY")

# Initialize the OpenAI client for Grok 3
client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1",
)

# Example: Make a chat completion request
completion = client.chat.completions.create(
    model="grok-3-beta",  # Replace with the correct model name if needed
    messages=[
        {"role": "system", "content": "You are Grok, a helpful assistant."},
        {"role": "user", "content": "check over all my code in all my modules, check for imporovments and make suggestions"},
    ],
)

# Print the response
print(completion.choices[0].message.content)