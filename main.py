import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

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

    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            ),
        )

        # Добавляем ответы модели в историю
        for candidate in response.candidates:
            messages.append(candidate.content)

        # Если нет function calls — финальный ответ
        if not response.function_calls:
            print(f"Final response:\n{response.text}")
            return

        # Обрабатываем function calls
        function_responses = []
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=args.verbose)

            if not function_call_result.parts:
                raise Exception("No parts in function call result")
            if function_call_result.parts[0].function_response is None:
                raise Exception("No function response in parts")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("No response in function response")

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

            function_responses.append(function_call_result.parts[0])

        # Добавляем результаты функций в историю
        messages.append(types.Content(role="user", parts=function_responses))

    print("Maximum iterations reached without a final response.")
    exit(1)

if __name__ == "__main__":
    main()