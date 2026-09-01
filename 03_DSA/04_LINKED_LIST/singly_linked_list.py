# Singly Linked List CRUD Playground

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert element at the end (Tail)
    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Delete first occurrence of value
    def delete(self, val):
        if not self.head:
            print("❌ List is empty!")
            return False

        # Case 1: Delete head node
        if self.head.val == val:
            self.head = self.head.next
            return True

        # Case 2: Traverse to locate target node
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next  # bypass node
                return True
            curr = curr.next
        
        print(f"❌ Value '{val}' not found in the list.")
        return False

    # Search for value
    def search(self, val):
        curr = self.head
        index = 0
        while curr:
            if curr.val == val:
                return index
            curr = curr.next
            index += 1
        return -1

    # Traverse list and return string representation
    def display(self):
        curr = self.head
        nodes = []
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return " -> ".join(nodes) + " -> None" if nodes else "Empty List -> None"

def main():
    ll = LinkedList()
    
    while True:
        print("\n--- Singly Linked List Menu ---")
        print("1. Insert (One or multiple separated by spaces)")
        print("2. Delete Value")
        print("3. Search Value")
        print("4. Display List")
        print("5. Exit")
        
        choice = input("Choose option (1-5): ").strip()
        
        if choice == "1":
            try:
                raw_input = input("Enter integer value(s) to insert: ")
                vals = [int(x) for x in raw_input.split()]
                for val in vals:
                    ll.insert(val)
                print(f"Added {vals} | Current list: {ll.display()}")
            except ValueError:
                print("❌ Invalid input. Please enter integers only.")
                
        elif choice == "2":
            try:
                val = int(input("Enter value to delete: "))
                if ll.delete(val):
                    print(f"Deleted {val} | Current list: {ll.display()}")
            except ValueError:
                print("❌ Invalid input.")
                
        elif choice == "3":
            try:
                val = int(input("Enter value to search: "))
                idx = ll.search(val)
                if idx != -1:
                    print(f"Found {val} at Index {idx}!")
                else:
                    print(f"Value {val} not found in the list.")
            except ValueError:
                print("❌ Invalid input.")
                
        elif choice == "4":
            print("Current List Structure:")
            print(ll.display())
            
        elif choice == "5":
            print("Keep coding! Bye-bye.")
            break
        else:
            print("Invalid Choice, try again.")

if __name__ == "__main__":
    main()
