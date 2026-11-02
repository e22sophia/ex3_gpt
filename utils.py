import os
from datetime import datetime
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"  # Change this if you downloaded a different Ollama model.

def ask_ollama(prompt):
    """Send a prompt to the locally running Ollama model."""
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            timeout=120
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.ConnectionError:
        return ("ERROR: Cannot connect to Ollama. Open another terminal and run "
                "'ollama serve', then check that your model is installed.")
    except requests.exceptions.Timeout:
        return "ERROR: Ollama took too long to respond. Try again."
    except requests.exceptions.RequestException as exc:
        return f"ERROR: Ollama request failed: {exc}"

def save_reply(customer_email, generated_reply, intent):
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/generated_reply.txt", "a", encoding="utf-8") as file:
        file.write("\\n" + "=" * 60 + "\\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n")
        file.write(f"Intent: {intent}\\n")
        file.write(f"Customer Email: {customer_email}\\n")
        file.write(f"Generated Reply:\\n{generated_reply}\\n")
    return "Reply saved to outputs/generated_reply.txt"
