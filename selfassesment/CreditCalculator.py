flag_value = int(input("Press 1 to stop application or a number greater than one: "))

while flag_value != 1:
    account = int(input("Enter the account number: "))
    beginBalance = int(input("Enter the balance at the beginning:"))
    item = int(input("Total of item charge by the customers monthly: "))
    credit = int(input("Total of credit applied: "))
    creditLimit = int(input("Allowed credit limit: "))
    newBalance = beginBalance + item - credit

    if newBalance > creditLimit:
        print(f"""
                                {account}
              {newBalance} is greater than credit Limit {creditLimit}
                        Credit limit already exceeded
                """)
    if newBalance <= creditLimit:
        print(f"""
                        {account}
        {newBalance} is less than or equal to credit Limit {creditLimit}
                        Credit limit not exceeded
        """)
    flag_value = int(input("Press 1 to stop or enter number not 1 to stop "))
