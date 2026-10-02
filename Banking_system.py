import json
import os

FILE = "accounts.json"


"Welcome To The My Banking System"

print("-"*50)
print("welcome to the VanshBank".title())
print("-"*50)


class VanshBank:
    """Represents  our bank account."""

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.__balance = balance

    def credit(self, amount):
      """Add money to the account."""
      if amount <= 0:
        print("Please enter a valid amount.")
        return False

      self.__balance += amount
      print(
          f"₹{amount} added to account "
          f"{self.account_no} successfully!"
      )
      return True

    def debit(self, amount):
      """Withdraw money from the account."""
      if amount <= 0:
          print("Please enter a valid amount.")
          return False

      if amount > self.__balance:
          print("Insufficient balance.")
          return False

      self.__balance -= amount
      print(
          f"₹{amount} withdrawn from account "
          f"{self.account_no} successfully!"
      )
      return True

    def check_balance(self):
        """Display current balance."""
        print(
            f"Current balance in account "
            f"{self.account_no}: ₹{self.__balance}"
        )

    def to_dict(self):
      return {
          "name": self.name,
          "account_no": self.account_no,
          "balance": self.__balance
      }



if os.path.exists(FILE):
    with open(FILE, "r") as f:
        data = json.load(f)
else:
    data = []

accounts = []

for account in data:
    obj = VanshBank(
        account["name"],
        account["account_no"],
        account["balance"]
    )

    accounts.append(obj)

def save_accounts():
    data = []

    for account in accounts:
        data.append(account.to_dict())

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
  
#Options for the services!!!
while True:
  
  print(
    """
     1.Add Account
     2.See Accounts
     3.withdraw The Money
     4.Dedosite The Money
     5.exit
    """
  )
  user=input("Choose the correct alternative from above".title()).lower()

  
  if user=="5":
    break
    
  elif user=="1":
    name = input("Enter your name: ")
    account_no = int(input("Enter The account number: "))
    balance = int(input("Enter initial balance To Adding In Your Account: "))

    new_account = VanshBank(name, account_no, balance)

    accounts.append(new_account)
    save_accounts()

    print("Account created successfully!\n\n\n")

  elif user == "2":
    if not accounts:
        print("No accounts found.\n\n\n")
    else:
        for account in accounts:
            print("-" * 30)
            print("Name:", account.name)
            print("Account Number:", account.account_no)
            account.check_balance()

  elif user == "3":
    account_no = int(input("Enter your account number: "))

    found_account = None

    for account in accounts:
        if account.account_no == account_no:
            found_account = account
            break

    if found_account is None:
        print("Account not found.")
    else:
        print("Account found!")
      
        amount = int(input("Enter amount to withdraw: "))
        success = found_account.debit(amount)

        if success:
          save_accounts()

  elif user == "4":
    account_no = int(input("Enter your account number: "))

    found_account = None

    for account in accounts:
        if account.account_no == account_no:
            found_account = account
            break

    if found_account is None:
        print("Account not found.")
    else:
        print("Account found!")

        amount = int(input("Enter amount to deposit: "))

        success = found_account.credit(amount)

        if success:
          save_accounts()
