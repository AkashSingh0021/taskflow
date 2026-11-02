import ollama
from prompts import PROMPT

def analyze_resume(resume_text):

    prompt = PROMPT.format(resume=resume_text)

    try:

        response = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error: {e}"