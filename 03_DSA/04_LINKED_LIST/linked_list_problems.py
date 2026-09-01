# Linked List Advanced Problems (Middle Node & Merge Sorted Lists)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Helper: Build list from array
def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

# Helper: Display list
def display_list(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(str(curr.val))
        curr = curr.next
    return " -> ".join(nodes) + " -> None" if nodes else "Empty -> None"

# 1. Find Middle Node (Fast & Slow Pointer)
def find_middle(head):
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 2. Merge Two Sorted Linked Lists (Dummy Node Technique)
def merge_sorted(l1, l2):
    dummy = Node(0)
    curr = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        
    curr.next = l1 if l1 else l2
    return dummy.next

def main():
    while True:
        print("\n--- Linked List Problems Menu ---")
        print("1. Find Middle Node (Fast & Slow Pointer)")
        print("2. Merge Two Sorted Lists")
        print("3. Exit")
        
        choice = input("Choose Option (1-3): ").strip()
        
        if choice == "1":
            try:
                raw = input("Enter list values (e.g. 1 2 3 4 5): ")
                vals = [int(x) for x in raw.split()]
                head = build_list(vals)
                print("List:", display_list(head))
                
                mid_node = find_middle(head)
                if mid_node:
                    print(f"Middle Node Value: {mid_node.val}")
                    print("Sublist from Middle:", display_list(mid_node))
                else:
                    print("List is empty!")
            except ValueError:
                print("Error: Please enter integers only.")
                
        elif choice == "2":
            try:
                raw1 = input("Enter List 1 (sorted, e.g. 1 3 5 7): ")
                raw2 = input("Enter List 2 (sorted, e.g. 2 4 6 8): ")
                
                vals1 = [int(x) for x in raw1.split()]
                vals2 = [int(x) for x in raw2.split()]
                
                l1 = build_list(vals1)
                l2 = build_list(vals2)
                
                print("List 1:", display_list(l1))
                print("List 2:", display_list(l2))
                
                merged_head = merge_sorted(l1, l2)
                print("Merged Sorted List:", display_list(merged_head))
            except ValueError:
                print("Error: Please enter integers only.")
                
        elif choice == "3":
            print("Keep rocking! Bye.")
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()

