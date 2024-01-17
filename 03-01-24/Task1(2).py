import json
import re

class BankAccount:
    # Static variable to keep track of the last account number
    last_account_number = 22426282425210

    def __init__(self, customer_name, phone_number, balance=0):
        self.__customer_name = customer_name
        self.__phone_number = self.__validate_phone_number(phone_number)
        self.__account_number = self.__generate_account_number()
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_customer_name(self):
        return self.__customer_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_phone_number(self):
        return self.__phone_number

    def to_json(self):
        return json.dumps({
            "customer_name": self.__customer_name,
            "account_number": self.__account_number,
            "balance": self.__balance,
            "phone_number": self.__phone_number
        })

    @staticmethod
    def from_json(json_string):
        data = json.loads(json_string)
        return BankAccount(data['customer_name'], data['phone_number'], data['balance'])

    def __generate_account_number(self):
        BankAccount.last_account_number += 1
        return str(BankAccount.last_account_number)

    def __validate_phone_number(self, phone_number):
        pattern = r'^[986][0-9]{9}$'
        if re.match(pattern, phone_number):
            return phone_number
        else:
            raise ValueError("Invalid phone number format")

    def save_to_file(self):
        try:
            with open('accounts.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        data[self.get_account_number()] = {
            "customer_name": self.get_customer_name(),
            "phone_number": self.get_phone_number(),
            "account_number": self.get_account_number(),
            "balance": self.get_balance()
        }
        with open('accounts.json', 'w') as file:
            json.dump(data, file)

    @staticmethod
    def admin_login(username, password):
        if username == 'admin' and password == 'Admin@SBI96':
            try:
                with open('accounts.json', 'r') as file:
                    data = json.load(file)
                    for account_number, account in data.items():
                        print(f"Account Number: {account_number}")
                        print(f"Customer Name: {account['customer_name']}")
                        print(f"Phone Number: {account['phone_number']}")
                        print(f"Balance: {account['balance']}\n")
            except FileNotFoundError:
                print("No accounts found.")
        else:
            print("Invalid admin credentials.")

    @staticmethod
    def user_login(account_number, phone_number):
        try:
            with open('accounts.json', 'r') as file:
                data = json.load(file)
                account_found = False
                for account in data.values():
                    if account.get('account_number') == account_number and account.get('phone_number') == phone_number:
                        print(f"Your Account Number: {account['account_number']}")
                        print(f"Your Balance: {account['balance']}")
                        account_found = True
                        break
                
                if not account_found:
                    print("Account not found.")
        except FileNotFoundError:
            print("No accounts found.")


while True:
    print("Welcome to the bank portal!")
    print("Enter 'exit' to quit.")

    user_type = input("Are you an admin or user? Enter 'admin' or 'user': ").lower()

    if user_type == 'exit':
        break

    if user_type == 'admin':
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        
        BankAccount.admin_login(username, password)
    elif user_type == 'user':
        account_number = input("Enter your account number: ")
        phone_number = input("Enter your phone number: ")
        
        BankAccount.user_login(account_number, phone_number)
    else:
        print("Invalid user type. Please enter 'admin' or 'user'.")
