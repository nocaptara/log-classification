from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()  # Changed 'groq' to 'client' for consistency

def classify_with_llm(log_msg):
    prompt = f'''Classify the log message into one of these categories:
    - Workflow Error
    - Deprecation Warning
    - Unclassified

    Only return one of the category names exactly as listed above, with no numbering, explanations, or extra words.
    Log message: {log_msg}'''

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    return chat_completion.choices[0].message.content.strip()  # Ensures clean output

if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))
