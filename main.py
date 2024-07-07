import openai

# OpenAIのAPIキーを設定
openai.api_key = 'your-api-key'

def generate_code(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    code = response.choices[0].text.strip()
    return code

import subprocess

def execute_code(code):
    try:
        exec(code, globals())
    except Exception as e:
        return str(e)
    return None

def generate_error_prompt(original_prompt, error_message):
    error_prompt = f"{original_prompt}\nThe above code produced the following error:\n{error_message}\nPlease provide a corrected version of the code."
    return error_prompt

def main():
    original_prompt = "Write a Python function that calculates the factorial of a number."
    code = generate_code(original_prompt)
    
    for _ in range(3):  # 最大3回まで試行
        print(f"Generated code:\n{code}")
        error = execute_code(code)
        if error is None:
            print("Code executed successfully.")
            break
        else:
            print(f"Error encountered: {error}")
            error_prompt = generate_error_prompt(original_prompt, error)
            code = generate_code(error_prompt)
    else:
        print("Failed to execute the code successfully after 3 attempts.")

if __name__ == "__main__":
    main()
