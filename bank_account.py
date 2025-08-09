class BankAccount:
    def __init__(self, balance=0.0):
        """Initialize the bank account with an optional starting balance."""
        self.balance = balance

    def deposit(self, amount):
        """Deposit the given amount and print the transaction."""
        self.balance += amount
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        """Withdraw the given amount if funds are sufficient."""
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.1f}")

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.balance:.2f}")
