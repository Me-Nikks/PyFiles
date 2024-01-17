import json
import re

class BankAccount:
    
    last_account_number = 22426282425210

    def __init__(self, customer_name, phone_number, balance=0):
        self.__customer_name = customer_name
        self.__phone_number = self.__validate_phone_number(phone_number)
        self.__account_number = self.__generate_account_number()
        self.__balance = balance

    @staticmethod
    def user_register(customer_name, phone_number):
        try:
            with open('accounts.json', 'r') as file:
                data = json.load(file)
                existing_phones = [account_data['phone_number'] for account_data in data.values()]
                if phone_number in existing_phones:
                    print("Phone number already exists. User registration failed.")
                    return
        except FileNotFoundError:
            pass

        new_account_number = str(BankAccount.last_account_number + 1)
        BankAccount.last_account_number = int(new_account_number)

        new_user = BankAccount(customer_name, phone_number)
        
        try:
            with open('accounts.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        data[new_user.get_account_number()] = {
            "customer_name": new_user.get_customer_name(),
            "phone_number": new_user.get_phone_number(),
            "account_number": new_user.get_account_number(),
            "balance": new_user.get_balance()
        }
        with open('accounts.json', 'w') as file:
            json.dump(data, file)

        print("User registered successfully!")
        print(f"Account Number: {new_user.get_account_number()}")
        print(f"Customer Name: {new_user.get_customer_name()}")
        print(f"Phone Number: {new_user.get_phone_number()}")
        print(f"Balance: {new_user.get_balance()}")



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

    def update_balance(account_number, new_balance):
        try:
            with open('accounts.json', 'r') as file:
                data = json.load(file)
                if data[account_number]['admin']:
                    data[account_number]['balance'] = new_balance
                    with open('accounts.json', 'w') as file:
                        json.dump(data, file)
                    print(f"Account {account_number} balance updated successfully.")
                else:
                    print("You don't have admin privileges to update the balance.")
        except FileNotFoundError:
            print("No accounts found.")


while True:
    print("Welcome to the SBI96!")
    print("Enter 'exit' to quit.")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Register")
    print("4. Update Account Balance (Admin Only)")

    user_choice = input("Enter your choice (1/2/3/4): ")

    if user_choice == 'exit':
        break

    if user_choice == '1':
        # Admin login logic
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        BankAccount.admin_login(username, password)

    elif user_choice == '2':
        # User login logic
        account_number = input("Enter your account number: ")
        phone_number = input("Enter your phone number: ")
        BankAccount.user_login(account_number, phone_number)

    elif user_choice == '3':
        # User registration logic
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        BankAccount.user_register(name, phone)

    elif user_choice == '4':
        # Update account balance (Admin Only)
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")

        if BankAccount.admin_login(admin_username, admin_password) == 'admin':
            acc_number = input("Enter the account number to update balance: ")
            new_balance = float(input("Enter the new balance: "))
            BankAccount.update_balance(acc_number, new_balance)

    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")

