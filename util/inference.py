import os
from openai import OpenAI

# Sync client for non-async operations
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv('OPENROUTER_API_KEY'),
)

def inference(messages: list[dict], model: str = "google/gemini-2.0-flash-001"):
    try:
        completion = openrouter_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
        response_content = completion.choices[0].message.content
        return response_content
        
    except Exception as e:
        raise Exception(f"Failed to generate outline: {e}")
