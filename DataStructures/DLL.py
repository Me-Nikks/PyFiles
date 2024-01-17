class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head == None:
            print("Empty Double linked list")
        else:
            temp = self.head
            while temp:
                print(temp.data, "---->",end='')
                temp = temp.next
            print('\n')

    def insert_beginning(self,data):
        n=Node(data)
        temp = self.head
        n.prev = temp
        n.next = temp
        self.head=n

    def insert_end(self,data):
        n= Node(data)
        if self.head == None:
            self.head = n
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = n
            n.prev = cur_node

    def insert_position(self,pos,data):
        n=Node(data)
        cur_node = self.head
        for i in range(1,pos-1):
            cur_node = cur_node.next
        n.prev = cur_node
        n.next = cur_node.next
        cur_node.next.prev = n
        cur_node.next = n
    
    def Dlt_beginning(self):
        cur_node = self.head
        self.head = cur_node.next
        cur_node.next = None

    def Dlt_end(self):
        cur_node = self.head
        if self.head == None:
            print("DLL is Empty")
        else:
            before = self.head
            cur_node=self.head.next
            while cur_node.next!=None:
                cur_node = cur_node.next #last node
                before = before.next #last but one node
            before.next = None
            cur_node.prev = None

    def Dlt_pos(self,pos):
        cur_node = self.head.next
        before = self.head
        for i in range (1,pos-1):
            cur_node = cur_node.next
            before = before.next

        before.next = cur_node.next
        cur_node.next.prev = before
        cur_node.next = None
        cur_node.prev = None
        
    

        


    





        




L = DLL()
n1=Node(11)
L.head = n1
n2=Node(12)
n3=Node(13)
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2

# L.insert_beginning(10)
# L.insert_end(55)
# L.insert_end(56)
# L.insert_end(69)
# L.insert_end(79)
# L.insert_end(89)
# L.insert_position(3,13)
# # L.insert_position(3,14)
# L.insert_position(2,14)
L.insert_position(3,155)
# L.insert_position(5,155)
# L.insert_position(6,155)
L.display()

# L.Dlt_beginning()


# L.Dlt_end()
# L.Dlt_end()
# L.Dlt_pos(4)
# L.Dlt_pos(2)
# L.Dlt_pos(3)





L.display()


        