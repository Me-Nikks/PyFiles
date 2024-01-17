class PlateStack:
    def __init__(self):
        self.stack = []

    def add_plate(self, plate):
        self.stack.append(plate)  # Adding a plate to the top of the stack
        print(f"Added '{plate}' to the stack of plates.")

    def remove_plate(self):
        if not self.stack:
            print("No plates in the stack.")
        else:
            removed_plate = self.stack.pop()  # Removing the top plate from the stack
            print(f"Removed '{removed_plate}' from the stack.")

# Creating an instance of PlateStack
plate_stack = PlateStack()

# Simulating the stacking and picking up of plates
plate_stack.add_plate("Plate1")
plate_stack.add_plate("Plate2")
plate_stack.add_plate("Plate3")

plate_stack.remove_plate()  
plate_stack.remove_plate()  
plate_stack.remove_plate()  
plate_stack.remove_plate()  
