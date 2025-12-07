class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on the account")

    def display_info(self):
        print(f"Bank Account No: {self.account_number}")
        formatted_balance = f"{self.balance:.2f}".replace('.', ',')
        print(f"Balance: PLN {formatted_balance}")