# programming_paradigm/main-0.py

import sys
from bank_account import BankAccount

def fmt_amount(amount):
    # Show integer without .0, otherwise trim trailing zeros.
    if amount is None:
        return ""
    if float(amount).is_integer():
        return str(int(float(amount)))
    s = f"{float(amount):.2f}".rstrip('0').rstrip('.')
    return s

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${fmt_amount(amount)}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${fmt_amount(amount)}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
