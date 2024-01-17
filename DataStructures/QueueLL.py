# QUEUE USING LinkedLIST 
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self):
        x=int(input("Enter the element to be inserted into Queue"))
        new=Node(x)
        if self.front is None:
            self.front=new
            self.rear=new
        else:
            self.rear.next = new
            self.rear = new

    def Dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        elif self.front.next is None:
            print("Popped Element is : ",self.front.data)
            
        else:
            cur = self.front
            print("Popped Element is : ", self.front.data)
            self.front=cur.next
            cur=None
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Elements of Queue are: ")
            cur= self.front
            while cur:
                print(cur.data, end='')
                cur=cur.next
                print()
    

q=Queue()

while(1):
        print("Enter your option")
        print("1. Enqueue \n2. Dequeue \n3. Display \n4. Exit")
        option = int(input())
        if option ==1:
            print("Enqueue Operation")
            q.enqueue()
        elif option ==2:
            print("Dequeue Operation")
            q.Dequeue()
        elif option ==3:
            print("Displaying operation")
            q.display()
        else:
            break






        