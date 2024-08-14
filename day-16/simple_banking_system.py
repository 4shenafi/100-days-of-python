import random


class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    accounts = []
    found = False
    while True:
        menu = int(input("MENU\n\t1. Create New Accounnt\n\t2. Deposit\n\t3. Withdraw\n\t4. Check Balance\nChoice: "))
        if menu == 1:
            while True:
                name = input("Enter full name of coustmer: ")
                account_number = 1000000000000 + random.randint(1, 100000000)
                accounts.append(BankAccount(account_number, name))
                print(f'Coustmer Added:\nname: {accounts[len(accounts) - 1].holder_name}\naccount number: '
                      f'{accounts[len(accounts) - 1].account_number}\nbalance: {accounts[len(accounts) - 1].balance}')
                ch = input("Want to add another coustmer?('y' or 'n'): ")
                if ch != 'y':
                    break
        elif menu == 2:
            account_number = int(input("Enter account number to deposit: "))
            for account in accounts:
                if account.account_number == account_number:
                    amount = int(input("Enter Amount to deposit: "))
                    account.deposit(amount)
                    found = True
                    print("Successfully Deposited!")
            if not found:
                print(f'{account_number} not found!')
        elif menu == 3:
            account_number = int(input("Enter account number to withdraw: "))
            for account in accounts:
                if account.account_number == account_number:
                    amount = int(input("How much do you want do withdraw: "))
                    account.withdraw(amount)
            if not found:
                print(f'{account_number} not found!')
        elif menu == 4:
            account_number = int(input("Enter account number to check balance: "))
            for account in accounts:
                if account.account_number == account_number:
                    print(f'Balance: {account.check_balance()}')
        choice = input("Would you like to continue?('y' or 'n'): ")
        if choice != 'y':
            break


