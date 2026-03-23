import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not found in environment variables.")
        return
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="ChatBot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = messages,
        config = types.GenerateContentConfig(system_instruction=system_prompt),
    )

    if response.usage_metadata == None:
        raise RuntimeError("Response does not contain usage metadata.")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
