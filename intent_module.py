from utils import ask_ollama

INTENTS = [
    "Delivery Issue",
    "Refund Request",
    "Product Complaint",
    "Technical Support",
    "Order Cancellation",
    "General Inquiry"
]

def detect_intent(customer_email):
    prompt = f"""
Classify the customer's email into exactly one of these categories:
{", ".join(INTENTS)}

Return only the category name, with no explanation.
Customer email: {customer_email}
"""
    result = ask_ollama(prompt)
    if result.startswith("ERROR:"):
        return "General Inquiry"
    for intent in INTENTS:
        if intent.lower() in result.lower():
            return intent
    return "General Inquiry"
