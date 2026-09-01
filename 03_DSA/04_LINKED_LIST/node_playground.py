# Custom Nodes and Traversal Playground

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(head):
    curr = head
    result = []
    # traverse until we hit None
    while curr:
        result.append(str(curr.val))
        curr = curr.next
    print("Linked Sequence:", " -> ".join(result) + " -> None")

def main():
    print("--- Let's build a linked sequence! ---")
    try:
        val1 = int(input("Enter value for Node 1: "))
        val2 = int(input("Enter value for Node 2: "))
        val3 = int(input("Enter value for Node 3: "))
        
        # 1. Create nodes
        n1 = Node(val1)
        n2 = Node(val2)
        n3 = Node(val3)
        
        # 2. Link them together
        n1.next = n2
        n2.next = n3
        
        print("\nNodes successfully linked!")
        # 3. Traverse and print
        print_list(n1)
        
    except ValueError:
        print("❌ Error: Please enter integers only!")

if __name__ == "__main__":
    main()

