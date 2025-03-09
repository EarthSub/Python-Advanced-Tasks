# On the first line, you will receive your bank account details, separated by a comma and a space,
# indicating your PIN code, initial balance, and age. Subsequently,
# you will receive a series of commands until the command "End":

#     "Send Money#{money}#{pin_code}"

#         · You should send money to your friend in need. Before the transaction, you must go through several validations:
#             o The money to be sent must be less than or equal to the initial balance, otherwise MoneyNotEnoughError should be raised.
#             o The given PIN code must match the initial one, otherwise, PINCodeError should be raised.
#             o To perform online transactions, you must be 18 or older, otherwise, UnderageTransactionError should be raised.
#         · If the transaction is successful, print on the console:
#             o "Successfully sent {amount_of_money} money to a friend"
#             o "There is {amount_of_money} money left in the bank account"
#             o The amount of money must be formatted to the second decimal place

#     "Receive Money#{money}"

#         · At the end of the month, you receive your salary. You invest half of the money in the stock market and the other half goes directly into the bank account:
#             o If the given money is a negative number, MoneyIsNegativeError, should be raised.
#         · If the operation is successful, print on the console:
#             o "{amount_of_money} money went straight into the bank account"
#             o The amount of money must be formatted to the second decimal place

# When an error is encountered, raise it with an appropriate message:

#     · MoneyNotEnoughError - "Insufficient funds for the requested transaction"
#     · PINCodeError - "Invalid PIN code"
#     · UnderageTransactionError - "You must be 18 years or older to perform online transactions"
#     · MoneyIsNegativeError - "The amount of money cannot be a negative number"


#                 Examples

# Input                           Output

# 9999, 3000, 18                  Successfully sent 1500.00 money to a friend
# Send Money#1500#9999            There is 1500.00 money left in the bank account
# Receive Money#2000              1000.00 money went straight into the bank account
# End

# Input                           Output

# 5545, 20000, 40                 Traceback (most recent call last):
# Send Money#15000#5455               File ".\online_banking.py", line 32, in <module>
# End                                     raise PINCodeError('Invalid PIN code')
#                                 PINCodeError: Invalid PIN code

# Input                           Output

# 2289, 1000, 17                  Traceback (most recent call last):
# Send Money#100#2289                 File ".\online_banking.py", line 35, in <module>
# End                                     raise UnderageTransactionError('You must be 18 years or
#                                 older to perform online transactions')
#                                 UnderageTransactionError: You must be 18 years or older to
#                                 perform online transactions

# Input                           Output

# 1234, 10000, 21                 Traceback (most recent call last):
# Send Money#10001#1234               File ".\online_banking.py", line 29, in <module>
# End                                     raise MoneyNotEnoughError('Insufficient funds for the
#                                 requested transaction')
#                                 MoneyNotEnoughError: Insufficient funds for the requested
#                                 transaction

# Input                           Output

# 1111, 7000, 50                  Traceback (most recent call last):
# Receive Money#-500                  File ".\online_banking.py", line 46, in <module>
# End                                     raise MoneyIsNegativeError('The amount of money cannot be a
#                                 negative number')
#                                 MoneyIsNegativeError: The amount of money cannot be a negative
#                                 number


class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, balance, age = [int(n) for n in input().split(", ")]
adult = age >= 18

while True:
    command = input()
    if command == "End":
        break

    action = command.split("#")
    if action[0] == "Send Money":
        money, pin = int(action[1]), int(action[2])
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")
        if not adult:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    if action[0] == "Receive Money":
        salary = int(action[1])
        if salary < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        deposit = salary / 2
        balance += deposit
        print(f"{deposit:.2f} money went straight into the bank account")
