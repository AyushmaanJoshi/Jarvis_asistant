import os  # Allows interaction with the operating system (not used directly here)
from azure.ai.inference import ChatCompletionsClient  # Lets us talk to the AI model
from azure.ai.inference.models import SystemMessage, UserMessage  # Used to format messages for the AI
from azure.core.credentials import AzureKeyCredential  # Helps securely send your secret key

# Your secret key to access the AI service (keep this private!)
token = "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"  # WARNING: Never share this in public code

# The web address where the AI model is hosted
endpoint = "https://models.github.ai/inference"

# The specific AI model you want to use
model = "openai/gpt-4.1"

# Create a client object to connect to the AI service using your endpoint and secret key
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def ask_ai_fallback(query):
    """
    This function sends your question to the AI and returns the answer.
    If something goes wrong, it tells you there was a problem.
    """
    try:
        # Send your question to the AI model
        response = client.complete(
            messages=[
                SystemMessage("You are a helpful assistant named Jarvis."),  # Tells the AI how to behave
                UserMessage(query),  # Your actual question to the AI
            ],
            temperature=1,  # Controls how creative the AI's answer is (higher = more creative)
            top_p=1,        # Another setting for creativity (1 = use all possible answers)
            model=model     # Which AI model to use
        )
        # Get the AI's answer from the response and remove extra spaces
        return response.choices[0].message.content.strip()
    except Exception as e:
        # If there was an error, print it and return a friendly message
        print("AI Fallback Error:", e)
        return "Sorry, I couldn’t get an answer from the assistant."
