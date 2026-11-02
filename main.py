from input_module import get_customer_details
from intent_module import detect_intent
from retrieval_module import retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import summarize_issue
from utils import save_reply

def process_email():
    name, subject, email = get_customer_details()

    print("\\n--- Intent Detection ---")
    intent = detect_intent(email)
    print("Detected Intent:", intent)

    print("\\n--- Similar Historical Email ---")
    previous = retrieve_similar_email(email)
    print("Previous Email:", previous["email"])
    print("Previous Reply:", previous["reply"])
    print("Similarity Score:", previous["score"])

    print("\\n--- Generated Professional Reply ---")
    reply = generate_reply(name, subject, email, intent, previous["reply"])
    print(reply)

    while True:
        print("\\nTone options: 1. Friendly  2. Formal  3. Empathetic  4. Keep original")
        choice = input("Choose a tone (1-4): ").strip()
        tones = {"1": "Friendly", "2": "Formal", "3": "Empathetic"}
        if choice in tones:
            reply = improve_tone(reply, tones[choice])
            print(f"\\n--- {tones[choice]} Tone Reply ---\\n{reply}")
            break
        if choice == "4":
            break
        print("Please enter 1, 2, 3, or 4.")

    print("\\n--- Conversation Summary (maximum 50 words) ---")
    print(summarize_issue(email))

    print("\\n" + save_reply(email, reply, intent))

def main():
    while True:
        print("\\n====== INTELLIGENT EMAIL ASSISTANT ======")
        print("1. Process a customer email")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            process_email()
        elif choice == "2":
            print("Thank you for using Intelligent Email Assistant.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
