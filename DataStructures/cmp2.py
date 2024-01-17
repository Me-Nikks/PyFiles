class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            cur = cur.next
            total += 1
        return total

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

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

        print("Index not found")
        return None

first = LinkedList()
first.append(111)
first.append(11)
first.display()
first.append(1122)
first.append(11)
first.display()
first.length()

print('element: %d' % first.get(3))  # Attempt to get element at index 3
