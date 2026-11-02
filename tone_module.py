from utils import ask_ollama

def improve_tone(reply, tone):
    prompt = f"""
Rewrite the email below in a {tone.lower()} tone.
Keep the meaning and facts unchanged. Do not add promises or new information.
Return only the rewritten email.

Email:
{reply}
"""
    result = ask_ollama(prompt)
    if result.startswith("ERROR:"):
        return reply
    return result
