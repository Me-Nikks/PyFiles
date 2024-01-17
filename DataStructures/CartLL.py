class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class MyCart:
    def __init__(self):
        self.head = node()

    def Add_item(self, data):
        new_item = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_item

    def Display_items(self):
        items = []
        cur_item = self.head.next
        while cur_item != None:
            items.append(cur_item.data)
            cur_item = cur_item.next
        print(items)

    def length(self):
        count = 0
        cur = self.head.next
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def Delete_item(self, index):
        if index >= self.length():
            print("Position Out of range")
            return

        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

cart = MyCart()

while True:
    print("\nSelect an action:")
    print("1. Add item to cart")
    print("2. Display items in the cart")
    print("3. Delete item")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        item = input("Enter the item to add: ")
        cart.Add_item(item)
        print(f"{item} added to the cart.")

    elif choice == 2:
        cart.Display_items()

    elif choice == 3:
        index = int(input("Enter the index of the item to delete: "))
        cart.Delete_item(index)

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
