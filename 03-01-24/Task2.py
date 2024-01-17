import re
import json

class AmazonWebsite:
    def __init__(self):
        self.load_from_json()
        self.admin = {'admin': 'Admin@123'}  # admin credentials

    def validate_password(self, password):
        # Password should contain at least one uppercase, one lowercase, one special character
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).+$"
        return re.match(regex, password)

    def user_sign_up(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different one.")
            return False

        if not self.validate_password(password):
            print("Password must contain at least one uppercase, one lowercase, and one special character.")
            return False

        self.users[username] = password
        print(f"User '{username}' signed up successfully!")
        self.save_to_json()  # Save updated user data to JSON file
        return True

    def user_login(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def admin_login(self, username, password):
        if username in self.admin and self.admin[username] == password:
            print(f"Welcome, Admin '{username}'!")
            return True
        else:
            print("Invalid admin credentials.")
            return False

    def display_user_details_dict(self, username, password):
        if self.admin_login(username, password):
            print("\nUser Details (Dictionary Format):")
            print(self.users)
        else:
            print("Only admin can access this information.")

    def display_user_details_json(self, username, password):
        if self.admin_login(username, password):
            print("\nUser Details (JSON Format):")
            print(json.dumps(self.users, indent=4))
        else:
            print("Only admin can access this information.")

    def save_to_json(self):
        with open('user_data.json', 'w') as file:
            json.dump(self.users, file)
        print("Data saved to user_data.json")

    def load_from_json(self):
        try:
            with open('user_data.json', 'r') as file:
                self.users = json.load(file)
            print("Data loaded from user_data.json")
        except FileNotFoundError:
            self.users = {}
            print("No existing data found.")


amazon = AmazonWebsite()

while True:
    print("\n1. User Sign-up")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Display User Details (Dictionary) [Admin Only]")
    print("5. Display User Details (JSON) [Admin Only]")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        amazon.user_sign_up(username, password)
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        amazon.user_login(username, password)
    elif choice == '3':
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        amazon.admin_login(username, password)
    elif choice == '4':
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        amazon.display_user_details_dict(username, password)
    elif choice == '5':
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        amazon.display_user_details_json(username, password)
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
