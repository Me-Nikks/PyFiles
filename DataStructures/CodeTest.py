# char = 'A' 
# print(ord(char))

# 2nd qustion 
'''
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def isPalindrome(head):
    if not head or not head.next:
        return True

    # Function to reverse a linked list
    def reverseList(node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    # Find the middle of the linked list
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    second_half = reverseList(slow.next)

    # Compare the first and reversed second halves
    first_half = head
    while second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

# Example usage:
# Create a palindrome linked list: 1 -> 2 -> 3 -> 3 -> 2 -> 1
palindrome_list = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))

# Check if it's a palindrome
result = isPalindrome(palindrome_list)
print(result)


'''


# 3rd Question
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    result = []
    stack = []
    
    if not root:
        return result

    stack.append(root)

    while stack:
        current = stack.pop()
        result.insert(0, current.val)

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    return result

root = TreeNode(100)
root.left = TreeNode(200)
root.right = TreeNode(300)
root.left.left = TreeNode(400)
root.left.right = TreeNode(500)

result = postorderTraversal(root)
print(result)

'''

#4th Question
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBST(root):
    def inorder_traversal(node):
        nonlocal prev_val

        if not node:
            return True

        # Check left subtree
        if not inorder_traversal(node.left):
            return False

        # Check current node
        if prev_val is not None and node.val <= prev_val:
            return False
        prev_val = node.val

        # Check right subtree
        return inorder_traversal(node.right)

    # Initialize prev_val to None before the first node
    prev_val = None

    # Start in-order traversal
    return inorder_traversal(root)

root = TreeNode(100)
root.left = TreeNode(50)
root.right = TreeNode(200)
root.left.left = TreeNode(25)
root.left.right = TreeNode(75)
root.right.left = TreeNode(150)
root.right.right = TreeNode(250)

result = isBST(root)
print(result)

'''

#5th question


'''
def isValidMathExpression(expression):
    stack = []

    # Dictionary to store the matching pairs of parentheses
    parentheses_pairs = {')': '(', ']': '[', '}': '{'}

    # Set of valid operators
    valid_operators = {'+', '-', '*'}

    for char in expression:
        if char in '({[':
            
            stack.append(char)
        elif char in ')}]':
            
            if not stack or stack.pop() != parentheses_pairs[char]:
                
                return 0
        elif char in valid_operators:
        
            if not stack or stack[-1] not in '0123456789':
                return 0
        elif char.isdigit():
            
            if stack and stack[-1] in valid_operators:
                stack.pop()

    
    return not stack

# Example usage:
example_one = "{(1+2)*3}+4"
example_two = "((1+2)*3*)"

output_one = isValidMathExpression(example_one)
output_two = isValidMathExpression(example_two)

print(output_one) 
print(output_two)  


'''

#6th Question

'''
def findMedianSortedArrays(arr, brr):
    if len(arr) > len(brr):
        arr, brr = brr, arr

    x, y = len(arr), len(brr)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxX = float('-inf') if partitionX == 0 else arr[partitionX - 1]
        maxY = float('-inf') if partitionY == 0 else brr[partitionY - 1]

        minX = float('inf') if partitionX == x else arr[partitionX]
        minY = float('inf') if partitionY == y else brr[partitionY]

        if maxX <= minY and maxY <= minX:
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1

# usage:
arr = [1, 2]
brr = [1, 4]

output = findMedianSortedArrays(arr, brr)
print(output)  


'''

# 7th Question 
'''
def isMatch(text, pattern):
    
    if not pattern:
        return not text

    # Check if the first characters match (or pattern has '.')
    first_match = bool(text) and (text[0] == pattern[0] or pattern[0] == '.')

    # Check if the pattern has '*'
    if len(pattern) >= 2 and pattern[1] == '*':
        # Two cases: (1) '*' matches zero characters, (2) '*' matches one or more characters
        return (isMatch(text, pattern[2:]) or
                (first_match and isMatch(text[1:], pattern)))
    else:
        # No '*' in pattern, match single character
        return first_match and isMatch(text[1:], pattern[1:])

# Example usage:
example1 = {"text": "abbbc", "pattern": "ab*c"}
example2 = {"text": "abcdefg", "pattern": "a.c.*.*gg*"}

output1 = isMatch(example1["text"], example1["pattern"])
output2 = isMatch(example2["text"], example2["pattern"])

print(output1)  # Output: 1
print(output2)  # Output: 1



'''

# 8th Question

'''
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




'''

# 9th Question 

'''
def push():
    n = int(input("Enter the element that needs to be in the stack: "))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0, n)
    print(n, " is added to the stack")

def pop():
    if len(stack) == 0:
        print("Stack is EMPTY!")
    else:
        print(stack[0], "is deleted")
        del stack[0]

def display():
    if len(stack) == 0:
        print("Stack is EMPTY!")
    else:
        print("Elements in STACK are:")
        for ele in stack:
            print(ele)
        print("Top of the stack is ", stack[0])

stack = list()
while True:
    print("Enter the option from below:")
    print("1. Push operation\n2. POP Operation\n3. Display")
    choice = int(input())
    if choice == 1:
        print("Push Operation")
        push()
    elif choice == 2:
        print("POP Operation")
        pop()
    elif choice == 3:
        print("Display Operation")
        display()
    else:
        print("Invalid input")
        break


'''

#10th Question
# '''
def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)

    # Initialize DP arrays for the two transactions
    buy1, sell1, buy2, sell2 = -prices[0], 0, float('-inf'), 0

    for i in range(1, n):
        # Update DP values for the first transaction
        buy1 = max(buy1, -prices[i])
        sell1 = max(sell1, buy1 + prices[i])

        # Update DP values for the second transaction
        buy2 = max(buy2, sell1 - prices[i])
        sell2 = max(sell2, buy2 + prices[i])

    # The final result is in sell2
    return max(0, sell2)

# Example usage:
prices1 = [3, 3, 5, 0, 0, 3, 1, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 4, 3, 1]

output1 = maxProfit(prices1)
output2 = maxProfit(prices2)
output3 = maxProfit(prices3)

print(output1)  
print(output2)  
print(output3)  



# '''
