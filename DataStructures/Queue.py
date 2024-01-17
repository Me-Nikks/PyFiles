# ENQUEUE > INSERTION > REAR END (-1)
# DEQUEUE > DELETION > FRONT END (0)
# QUEUE USING LIST 
def enqueue():
    n=int(input("Enter the element to be inserted into Queue"))
    queue.append(n)
    print()

def dequeue():
    if len(queue)==0:
        print("QUEUE IS EMPTY")
        print()
    else:
        print(queue[0]," is deleted from Queue")
        del queue[0]-
        
        print()

def display():
    if len(queue)==0:
        print("QUEUE IS EMPTY")
        print()
    else:
        print("Queue Elements are:")
        for ele in queue:
            print(ele,end=' '"\n")
        print("Front of the queue is ", queue[0])
        print("Rear of the queue is ", queue[-1])

queue = list()
while(1):
    print("Enter your option")
    print("1. Enqueue \n2. Dequeue \n3. Display \n4. Exit")
    option = int(input())
    if option ==1:
        print("Enqueue Operation")
        enqueue()
    elif option ==2:
        print("Dequeue Operation")
        dequeue()
    elif option ==3:
        print("Displaying the queue")
        display()
    else:
        break



