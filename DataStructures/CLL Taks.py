import pandas as pd

class Node:
    def __init__(self, filename):
        self.filename = filename
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # def insert(self, filename):
    #     new_node = Node(filename)
    #     if not self.head:
    #         self.head = new_node
    #         new_node.next = self.head
    #     else:
    #         temp = self.head
    #         while temp.next != self.head:
    #             temp = temp.next
    #         temp.next = new_node
    #         new_node.next = self.head

    # def display(self):
    #     if not self.head:
    #         print("List is empty")
    #     else:
    #         temp = self.head
    #         while True:
    #             print(temp.filename, end=" -> ")
    #             temp = temp.next
    #             if temp == self.head:
    #                 break
    #         print()

    # def read_excel(self):
    #     if self.head:
    #         print(f"Reading CSV file: {self.head.filename}")
            
    #         data = pd.read_csv(self.head.filename)
    #         print(data)
    #     else:
    #         print("List is empty")

if __name__ == "__main__":
    
    csv_files = [r"C:\\Users\\Admin\\Desktop\\file1.csv", r"C:\\Users\\Admin\\Desktop\\file2.csv"]

    circular_list = CircularLinkedList()

    for file in csv_files:
        circular_list.insert(file)

    while True:
        print("Press 'n' for next page, 'p' for previous page, 'r' to read CSV, or 'q' to quit:")
        choice = input().lower()

        if choice == 'n':
            circular_list.head = circular_list.head.next
        elif choice == 'p':
            temp = circular_list.head
            while temp.next != circular_list.head:
                temp = temp.next
            circular_list.head = temp
        elif choice == 'r':
            circular_list.read_excel()
        elif choice == 'q':
            break

        circular_list.display()
