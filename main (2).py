class BankAccount:
   def __init__(self, account_number, account_holder_name, initial_balance):
       self.__account_number = account_number
       self.__account_holder_name = account_holder_name
       self.__account_balance = initial_balance

   def deposit(self, amount):
       if amount > 0:
           self.__account_balance += amount
           return f'Deposit of ${amount} successful. New balance is ${self.__account_balance}.'
       else:
           return "Invalid amount. Please enter a positive value."

   def withdraw(self, amount):
       if amount > 0 and amount <= self.__account_balance:
           self.__account_balance -= amount
           return f'Withdrawal of ${amount} successful. New balance is ${self.__account_balance}.'
       elif amount > self.__account_balance:
           return "Insufficient funds. Withdrawal failed."
       else:
           return "Invalid amount. Please enter a positive value."

   def display_balance(self):
       return f'Account Balance for {self.__account_holder_name}: ${self.__account_balance}'


 # Testing the BankAccount class
account = BankAccount("123456", "John Doe", 1000)

print(account.display_balance())  # Output: Account Balance for John Doe: $1000

print(account.deposit(500))  # Output: Deposit of $500 successful. New balance is $1500.
print(account.display_balance())  # Output: Account Balance for John Doe: $1500

print(account.withdraw(200))  # Output: Withdrawal of $200 successful. New balance is $1300.
print(account.display_balance())  # Output: Account Balance for John Doe: $1300

print(account.withdraw(1500))  # Output: Insufficient funds. Withdrawal failed.
