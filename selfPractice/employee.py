class employee:
    def __init__(self, first_name, last_name,email,DOB):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.DOB = DOB

    def check_age(self):
        #date format dd-mm-yyyy
        birth_year = int(self.DOB.split('-')[2])
        current_year = 2023
        age = current_year - birth_year

        if age >=55:
            print(f"hey {self.last_name} you are above 55")

        else:
            print(f"hey {self.last_name} you are below 55")
    
    def check_email(self):
        if '@' in self.email:
            print("This is a valid email")
        else:
            print("This is not a valid email")

emp1 = employee("Manu", "Sharma", "manu@katte.com", "22-12-2011")
emp1.check_age()
emp1.check_email()


emp2 = employee("Raj", "gopal", "raj.raja", "12-02-1965")
emp2.check_age()
emp2.check_email()

     