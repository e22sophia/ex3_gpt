from utils import ask_ollama

def summarize_issue(customer_email):
    prompt = f"""
Summarize the customer's issue in no more than 50 words.
Do not invent details. Return only the summary.

Customer email: {customer_email}
"""
    result = ask_ollama(prompt)
    if result.startswith("ERROR:"):
        return "The customer has contacted support with an issue that requires review and an appropriate follow-up."
    return result
