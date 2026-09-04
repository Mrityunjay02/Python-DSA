# Binary Tree & BST Core Problems (Max Depth, Invert Tree, Validate BST)
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build Tree dynamically from level-order input
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        curr = queue.popleft()
        if i < len(values) and values[i] is not None:
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
        i += 1
        if i < len(values) and values[i] is not None:
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
        i += 1
    return root

# Display Level Order
def display_tree(root):
    if not root:
        return "Empty Tree"
    levels = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current = []
        for _ in range(level_size):
            node = queue.popleft()
            current.append(str(node.val))
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        levels.append("[ " + ", ".join(current) + " ]")
    return " -> ".join(levels)

# 1. Max Depth of Binary Tree
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# 2. Invert Binary Tree
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

# 3. Validate Binary Search Tree (BST)
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    return (is_valid_bst(root.left, min_val, root.val) and 
            is_valid_bst(root.right, root.val, max_val))

def main():
    root = None
    while True:
        print("\n--- Tree Core Problems Menu ---")
        print("1. Build / Change Tree (Keyboard input, e.g. 4 2 7 1 3 6 9)")
        print("2. Calculate Maximum Depth / Height")
        print("3. Invert Tree (Mirror Flip)")
        print("4. Check if Tree is Valid BST")
        print("5. Display Tree Structure")
        print("6. Exit")
        
        choice = input("Choose Option (1-6): ").strip()
        
        if choice == "1":
            try:
                raw = input("Enter tree node values (spaces): ")
                vals = [int(x) if x.lower() != 'none' and x.lower() != 'null' else None for x in raw.split()]
                root = build_tree(vals)
                print(f"Tree built! Current Structure: {display_tree(root)}")
            except ValueError:
                print("Error: Please enter numbers only.")
                
        elif choice == "2":
            if not root:
                print("Tree is empty! Build tree first (Option 1).")
            else:
                depth = max_depth(root)
                print(f"🟢 Maximum Depth / Height of Tree: {depth}")
                
        elif choice == "3":
            if not root:
                print("Tree is empty!")
            else:
                print("Before Invert:", display_tree(root))
                invert_tree(root)
                print("🟢 After Invert (Mirror):", display_tree(root))
                
        elif choice == "4":
            if not root:
                print("Tree is empty!")
            else:
                if is_valid_bst(root):
                    print("🟢 VALID BST! Left < Root < Right rule strictly satisfied.")
                else:
                    print("🔴 INVALID BST! Tree violates Binary Search Tree invariant.")
                    
        elif choice == "5":
            print("Current Tree Levels:", display_tree(root))
            
        elif choice == "6":
            print("done.")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()

