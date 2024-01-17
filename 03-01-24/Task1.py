import json
import time
import re

class BankAccount:
    def __init__(self, customer_name, phone_number, balance=0):
        self.__customer_name = customer_name
        self.__phone_number = self.__validate_phone_number(phone_number)
        self.__account_number = self.__generate_unique_account_number()
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

    def __generate_unique_account_number(self):
        while True:
            new_account_number = self.__generate_account_number()
            if not self.__check_duplicate_account_number(new_account_number):
                return new_account_number

    def __check_duplicate_account_number(self, account_number):
        try:
            with open('accounts.json', 'r') as file:
                data = json.load(file)
                for account in data.values():
                    if 'account_number' in account and account['account_number'] == account_number:
                        return True
        except (FileNotFoundError, KeyError):
            return False
        return False


    def __generate_account_number(self):
        timestamp = str(int(time.time())) * 8
        # constant_digits = '00000000'  # 8 constant digits
        account_number = '42628292' + timestamp
        return int(account_number[:14])

    def __validate_phone_number(self, phone_number):
        pattern = r'^[986][0-9]{9}$'  # Phone number starts with 9, 8, or 6 and has a length of 10
        if re.match(pattern, phone_number):
            return phone_number
        else:
            raise ValueError("Invalid phone number format")

    def save_to_file(self):
        # Save account details to a JSON file
        try:
            with open('accounts.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        data[self.get_account_number()] = {
            "customer_name": self.get_customer_name(),
            "phone_number": self.get_phone_number(),
            "balance": self.get_balance()
        }
        with open('accounts.json', 'w') as file:
            json.dump(data, file)

class CurrentAccount(BankAccount): 
    transaction_limit = 50000

    def __init__(self, customer_name, phone_number, balance=0):
        super().__init__(customer_name, phone_number, balance)
        self.save_to_file()

class SavingsAccount(BankAccount):
    transaction_limit = 20000

    def __init__(self, customer_name, phone_number, balance=0):
        super().__init__(customer_name, phone_number, balance)
        self.save_to_file()

# Example usage
das_account = CurrentAccount('Nikhildas', '9876543210', 2000)
ziya_account = SavingsAccount('Ziya', '8765432109', 20000)

# Convert to JSON and print
das_json = das_account.to_json()
ziya_json = ziya_account.to_json()
print(das_json)
print(ziya_json)

# Convert back from JSON and access data
restored_das_account = BankAccount.from_json(das_json)
print(restored_das_account.get_customer_name())
print(restored_das_account.get_balance())
print(restored_das_account.get_account_number())
print(restored_das_account.get_phone_number())
