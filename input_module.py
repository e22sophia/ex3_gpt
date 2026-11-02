def get_customer_details():
    print("\\n--- Customer Email Details ---")
    name = input("Customer Name: ").strip()
    subject = input("Email Subject: ").strip()
    email = input("Customer Email: ").strip()

    print("\\n--- Entered Details ---")
    print("Customer Name:", name)
    print("Subject:", subject)
    print("Customer Email:", email)
    return name, subject, email
