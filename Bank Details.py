class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
        else:
            print("Insufficient funds for withdrawal.")

    def get_balance(self):
        return self.balance

# User input for account creation
account_holder = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_holder, initial_balance)

while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        deposit_amount = float(input("Enter the deposit amount: "))
        account.deposit(deposit_amount)
    elif choice == '2':
        withdraw_amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(withdraw_amount)
    elif choice == '3':
        print(f"Current balance: ${account.get_balance()}")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")

