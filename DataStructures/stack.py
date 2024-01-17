# last in first out
# push: Insertion --> Top
# pop: Deletion --> Top

# Implementation - 2 Types 
# -> Using list
# -> Using linked List
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

    
