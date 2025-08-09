# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # public attribute name as required by the task
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to account_balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the amount if funds are sufficient.
        Return True if withdrawal succeeded, otherwise False.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current balance exactly like:
          Current Balance: $100.00
          Current Balance: $100.50
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
