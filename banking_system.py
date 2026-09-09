# Python Banking System
# Created by Vanshkumar Bankar
# A simple banking system built to practice Python OOP concepts.


class VanshBank:
    """Represents a basic bank account."""

    def __init__(self, name, account_no, balance):
        # Account information
        self.name = name
        self.account_no = account_no

        # Private balance
        self.__balance = balance

    def credit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            print("Please enter a valid amount.".title())
            return

        self.__balance += amount
        print(
            f"₹{amount} added to account "
            f"{self.account_no} successfully!"
        )

    def debit(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Please enter a valid amount.".title())
            return

        if amount > self.__balance:
            print("this Much balance Is Not in your Account.".title())
        else:
            self.__balance -= amount
            print(
                f"₹{amount} withdrawn from account "
                f"{self.account_no} successfully!"
            )

    def check_balance(self):
        """Display the current account balance."""
        print(
            f"Current balance in account "
            f"{self.account_no}: ₹{self.__balance}"
        )


# Creating bank accounts
account1 = VanshBank("Vansh", 1234567890, 500)
account2 = VanshBank("Rakesh", 650979304737, 1000)

# Checking initial balances
account1.check_balance()
account2.check_balance()

# Adding money to Rakesh's account
account2.credit(1000)

# Checking updated balance
account2.check_balance()
