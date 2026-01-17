import argparse
import os

# from runpy import run_module
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    if args.user_prompt is None:
        raise RuntimeError("Missing argument 'User prompt'.")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError(
            "API key not found. Please set the GEMINI_API_KEY "
            "environment variable in your .env file."
        )

    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    model_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )

    if model_response.usage_metadata is None:
        raise RuntimeError("There was no response from client.")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {model_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {model_response.usage_metadata.candidates_token_count}")

    print(f"Response: {model_response.text}")


if __name__ == "__main__":
    main()
