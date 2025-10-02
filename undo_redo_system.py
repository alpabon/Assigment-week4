# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value
    
    def print_stack(self):
        if not self.top:
            print("Stack is empty")
            return
        current = self.top
        while current:
            print(current.value)
            current = current.next

    def is_empty(self):
        return self.top is None

def run_undo_redo():
    undo_stack = Stack()
    redo_stack = Stack()
    # Create instances of the Stack class for undo and redo
    

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            # Push the action onto the undo stack and clear the redo stack


            print(f"Action performed: {action}")
        elif choice == "2":
            if undo_stack.is_empty():
                print("No actions to undo")
                continue
            else:
                action = undo_stack.pop()
                redo_stack.push(action)
            # Pop an action from the undo stack and push it onto the redo stack
            

        elif choice == "3":
            if redo_stack.is_empty():
                print("No actions to redo")
                continue
            else:
                action = redo_stack.pop()
                undo_stack.push(action)
            # Pop an action from the redo stack and push it onto the undo stack


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()

            
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()


    #Why is a stack the right choice for undo/redo?
    #A stack is the right choice for undo/redo because it follows the Last In, First Out (LIFO) principle. This means that the most recent action performed is the first one to be undone, which is perfect for how the users expect to undo functionality to work. When an action is undone, it can be pushed onto a redo stack, allowing users to redo actions in the reverse order they were undone.
#Why is a queue better suited for the help desk?
    #A queue is better suited for the help desk because it follows the First In, First Out (FIFO) principle. This means that customers are helped in the order they arrive. The first customer to enter the queue is the first one to be served, which is the normal situations when customer services are helping clients.
#How do your implementations differ from Python’s built-in lists?
    #My implementations differ from pythons built-in lists because they are specifically designed to funcion as stacks and queues, also they have methods of data structures ( like push, pop for stacs and enqueue,dequeue for queues). built-in lists in pyhton are more general and not such an especific purpose and our data structures are fare mor efficient. also with the implementation of th eLIFO AND FIFO principles and linked nodes, the system is more memory efficient and time efficient
