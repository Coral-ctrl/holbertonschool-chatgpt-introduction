#!/usr/bin/python3
class Checkbook:
    """
    Class representing a simple checkbook with deposit, withdrawal, and balance functionality.
    """
    def __init__(self):
        """
        Initializes the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds the specified amount to the balance.

        Parameters:
        amount (float): The amount to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Subtracts the specified amount from the balance if sufficient funds exist.

        Parameters:
        amount (float): The amount to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main program loop that prompts the user to deposit, withdraw, check balance, or exit.
    Handles invalid input gracefully.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
