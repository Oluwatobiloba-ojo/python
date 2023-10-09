from finanace.Finance import credit_card_type, validate_credit_cards

card_details = input("Hello, Kindly Enter Card Details To Verify")
card_type = credit_card_type(card_details)
card_validation = validate_credit_cards(card_details)
card_length = len(card_details)
print(f"""
    *************************************************
    **Credit Card Type: {card_type}
    **Credit Card Number: {card_details}
    **Credit Card Digit Length: {card_length}
    **Credit Card Validity Status: {card_validation}
    **************************************************
    """)