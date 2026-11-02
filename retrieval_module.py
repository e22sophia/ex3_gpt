import csv
import os
from difflib import SequenceMatcher

def retrieve_similar_email(customer_email, csv_path="data/emails.csv"):
    if not os.path.exists(csv_path):
        return {"email": "No dataset found.", "reply": "No previous reply available.", "score": 0}

    best_row = None
    best_score = -1
    query = customer_email.lower()

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            old_email = row.get("Customer_Email", row.get("Email", "")) or ""
            score = SequenceMatcher(None, query, old_email.lower()).ratio()
            if score > best_score:
                best_score = score
                best_row = row

    if not best_row:
        return {"email": "No previous email found.", "reply": "No previous reply available.", "score": 0}

    old_email = best_row.get("Customer_Email", best_row.get("Email", ""))
    old_reply = best_row.get("Previous_Reply", best_row.get("Reply", "No previous reply available."))
    return {"email": old_email, "reply": old_reply, "score": round(best_score, 3)}
