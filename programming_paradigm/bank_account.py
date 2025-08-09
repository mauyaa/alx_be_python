# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # public attribute name as required by the task
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to account_balance."""
        # accept numeric input (int/float)
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
          Current Balance: $100
        or when not whole:
          Current Balance: $100.50
        """
        bal = self.account_balance
        # If it's a float equal to integer, show as integer
        try:
            # handle float-like values
            if isinstance(bal, float) and bal.is_integer():
                print(f"Current Balance: ${int(bal)}")
            else:
                # strip unnecessary trailing zeros for floats
                if isinstance(bal, float):
                    s = f"{bal:.2f}".rstrip('0').rstrip('.')
                    print(f"Current Balance: ${s}")
                else:
                    print(f"Current Balance: ${bal}")
        except Exception:
            # fallback to simple print
            print(f"Current Balance: ${bal}")
