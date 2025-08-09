# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if funds are sufficient.
        Return True if withdrawal succeeded, otherwise False.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
