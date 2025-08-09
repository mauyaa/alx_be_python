#!/usr/bin/env python3
"""
BankAccount class for ALX task.
Supports deposit, withdraw, and display methods with required messages.
"""

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with optional initial balance."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Add amount to balance."""
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """Subtract amount from balance if funds are sufficient."""
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def display(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.balance}")
