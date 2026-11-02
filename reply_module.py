from utils import ask_ollama

def generate_reply(customer_name, subject, customer_email, intent, previous_reply):
    prompt = f"""
You are a professional customer-support email assistant.
Write a helpful, professional email reply to the customer.
Use the previous reply as reference when relevant, but do not copy it blindly.
Do not invent order numbers, refunds, delivery dates, or actions that are not confirmed.
Keep the response concise. Include a greeting and sign off as Support Team.

Customer name: {customer_name}
Subject: {subject}
Detected intent: {intent}
Customer email: {customer_email}
Similar historical email reply: {previous_reply}

Write only the email reply.
"""
    result = ask_ollama(prompt)
    if result.startswith("ERROR:"):
        return ("Dear Customer,\\n\\nThank you for contacting our support team. "
                "We are sorry for the inconvenience. Our team will review your concern "
                "and follow up with you as soon as possible.\\n\\nRegards,\\nSupport Team")
    return result
