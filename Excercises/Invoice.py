user_name = input("Enter your name: ")
user_item = input("Enter the item bought:")
user_price = int(input("Enter the price of item your item bought : "))
credit_score = bool(input("(Enter 1 for good credit score) (Enter (Enter) bad credit score) "))
if credit_score:
    discount = 10 * user_price / 100
    discount_price = user_price - discount
    deposit_payment = 10 * discount_price / 100
    print(f"""
    ****************************
    INVOICE
    ****************************
    NAME OF BUYERS: {user_name}
    NAME OF ITEMS: {user_item}
    DISCOUNT: {discount}
    DEPOSIT: {deposit_payment:.2f}
    ****************************
    """)
else:
    deposit_amount = 25 * user_price / 100
    print(f"""
    ***************************
    INVOICE
    ***************************
    NAME OF BUYERS:{user_name}
    NAME OF ITEMS:{user_item}
    DISCOUNT: No discount cause you had bad credit score
    DEPOSIT AMOUNT: {deposit_amount :.2f}
    ***************************
    """)