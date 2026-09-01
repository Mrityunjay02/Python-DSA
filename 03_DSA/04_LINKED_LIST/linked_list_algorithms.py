# Linked List Core Algorithms Demonstration

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert element
    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Reverse List (Iterative)
    def reverse(self):
        prev = None
        curr = self.head
        
        while curr:
            next_node = curr.next  # save reference
            curr.next = prev       # reverse link
            prev = curr            # shift prev
            curr = next_node       # shift curr
            
        self.head = prev

    # Floyd's Cycle Detection
    def detect_loop(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # Force a loop back to a specific value index for testing
    def create_loop(self, target_val):
        if not self.head:
            return
            
        target_node = None
        curr = self.head
        tail = None
        
        while curr:
            if curr.val == target_val:
                target_node = curr
            if not curr.next:
                tail = curr
            curr = curr.next
            
        if tail and target_node:
            tail.next = target_node  # creates loop back to target node!
            print(f"Loop created successfully from Tail ({tail.val}) back to Node ({target_node.val})!")
        else:
            print("❌ Target value not found to create loop.")

    def display(self):
        # Prevent infinite loop during display if list has a cycle!
        visited = set()
        curr = self.head
        nodes = []
        
        while curr:
            if curr in visited:
                nodes.append(f"LOOP BACK TO {curr.val}...")
                break
            visited.add(curr)
            nodes.append(str(curr.val))
            curr = curr.next
            
        return " -> ".join(nodes) + " -> None" if nodes else "Empty List -> None"

def main():
    ll = LinkedList()
    
    while True:
        print("\n--- Linked List Algorithms ---")
        print("1. Insert Values (space-separated)")
        print("2. Reverse List")
        print("3. Check Cycle / Loop")
        print("4. Force Create Loop (for testing)")
        print("5. Display List")
        print("6. Exit")
        
        choice = input("Option (1-6): ").strip()
        
        if choice == "1":
            try:
                raw_input = input("Enter values (spaces): ")
                vals = [int(x) for x in raw_input.split()]
                for val in vals:
                    ll.insert(val)
                print("List:", ll.display())
            except ValueError:
                print("Error: Invalid inputs.")
                
        elif choice == "2":
            if ll.detect_loop():
                print("❌ Cannot reverse a list with an infinite loop!")
            else:
                ll.reverse()
                print("Reversed List:", ll.display())
                
        elif choice == "3":
            if ll.detect_loop():
                print("🟢 Cycle detected in the list! (Infinite loop exists)")
            else:
                print("🔴 No cycle detected. List ends safely at None.")
                
        elif choice == "4":
            if not ll.head:
                print("❌ Create list first.")
            else:
                try:
                    target = int(input("Enter node value to loop back to: "))
                    ll.create_loop(target)
                except ValueError:
                    print("Invalid input.")
                    
        elif choice == "5":
            print("List Structure:", ll.display())
            
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

