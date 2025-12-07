from bank_account import BankAccount

def main():
    account = BankAccount("12 3456 5555 9090 1111 0000 7722")
    
    account.display_info()
    
    account.deposit(25.30)
    account.display_info()
    
    account.withdraw(31.70)
    account.display_info()
    
    account.withdraw(14)
    account.display_info()

if __name__ == "__main__":
    main()