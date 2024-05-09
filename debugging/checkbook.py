class Checkbook:
    """
    A class representing a simple checkbook.

    Attributes:
        balance (float): The current balance in the checkbook.
    """
    def __init__(self):
        """
        Initialize the Checkbook object with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit an amount into the checkbook.

        Parameters:
            amount (float): The amount to be deposited.
        """
        if amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw an amount from the checkbook.

        Parameters:
            amount (float): The amount to be withdrawn.
        """
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance in the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    The main function to interact with the Checkbook object.
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
                print("Invalid input. Please enter a valid amount.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
