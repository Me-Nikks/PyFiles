class node:
    def __init__(self,data=None,next=None):
        self.data= data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            cur = cur.next
            total += 1
        return total
    
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

    # def get(self,index):
    #     if index>=self.length() or index < 0:
    #         print("Index out of range")
    #         return None
        
    #     cur_idx = 0
    #     cur_node=self.head.next
    #     while cur_node!=None:
    #         if cur_idx == index:
    #             return cur_node.data
    #         cur_node = cur_node.next
    #         cur_idx +=1
        
    def get(self, index):
        if index >= self.length() or index < 0:  # Updated condition to check if index is out of range
            print("Index out of range")
            return None

        cur_idx = 0
        cur_node = self.head.next  # Start from the first node
        while cur_node is not None:
            if cur_idx == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_idx += 1

        print("not found")
        return None
    
    def erase(self,index):
        if index>=self.length():
            print("Index Out of range")
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx +=1

        


    
        
first = LinkedList()
first.append(111)
first.append(11)
first.display()
first.append(1122)
first.append(11)
first.display()
first.erase(1)
first.display()

print('element: %d' % first.get(3))