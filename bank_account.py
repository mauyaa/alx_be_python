class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount > 0:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Invalid withdrawal amount."

    def display_balance(self):
        return f"Current balance: ${self.balance:.2f}"
