import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def get_text_response(input_content):
    # Initialize OpenAI client
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    # Create chat completion
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Note: OpenAI doesn't have a direct equivalent to Claude 3 Sonnet
        messages=[
            {
                "role": "user",
                "content": input_content
            }
        ],
        max_tokens=2000,
        temperature=0,
        top_p=0.9,
        stop=None  # OpenAI API doesn't have a direct equivalent to stopSequences
    )

    # Extract and return the response text
    return chat_completion.choices[0].message.content