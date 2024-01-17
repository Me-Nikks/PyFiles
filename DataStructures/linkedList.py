class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

if __name__ == 'main':
    ll = LinkedList()
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(69)        
    ll.insert_at_beginning(77)  
    ll.print()      