#!/usr/bin/env python3
import sys
from programming_paradigm.bank_account import BankAccount

account = BankAccount(100)  # Example starting balance

if len(sys.argv) > 1:
    if sys.argv[1] == "display":
        account.display()
    elif sys.argv[1] == "withdraw":
        if len(sys.argv) > 2:
            account.withdraw(float(sys.argv[2]))
    elif sys.argv[1] == "deposit":
        if len(sys.argv) > 2:
            account.deposit(float(sys.argv[2]))
