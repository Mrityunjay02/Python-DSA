# Doubly Linked List Operations

class DLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert element at the end (Tail)
    def insert(self, val):
        new_node = DLLNode(val)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        new_node.prev = curr  # Link previous node

    # Traverse forward
    def display_forward(self):
        curr = self.head
        nodes = []
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return " -> ".join(nodes) + " -> None" if nodes else "Empty List -> None"

    # Traverse backward
    def display_backward(self):
        if not self.head:
            return "Empty List -> None"
            
        curr = self.head
        while curr.next:
            curr = curr.next
            
        nodes = []
        while curr:
            nodes.append(str(curr.val))
            curr = curr.prev
        return " -> ".join(nodes) + " -> None"

def main():
    dll = DoublyLinkedList()
    
    while True:
        print("\n--- Doubly Linked List ---")
        print("1. Insert")
        print("2. Display Forward")
        print("3. Display Backward")
        print("4. Exit")
        
        choice = input("Option (1-4): ").strip()
        
        if choice == "1":
            try:
                raw_input = input("Enter values (spaces): ")
                vals = [int(x) for x in raw_input.split()]
                for val in vals:
                    dll.insert(val)
                print("List (Forward):", dll.display_forward())
            except ValueError:
                print("Error: Invalid input.")
                
        elif choice == "2":
            print("Forward:", dll.display_forward())
            
        elif choice == "3":
            print("Backward:", dll.display_backward())
            
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

