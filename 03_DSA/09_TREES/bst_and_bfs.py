# Binary Search Tree (BST) & BFS Level Order Traversal
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 1. BST Insert (Maintains Left < Root < Right)
def bst_insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    elif val > root.val:
        root.right = bst_insert(root.right, val)
    return root

# 2. BST Search (O(log N))
def bst_search(root, target):
    if not root or root.val == target:
        return root
    if target < root.val:
        return bst_search(root.left, target)
    return bst_search(root.right, target)

# 3. Inorder Traversal (Always sorted for BST)
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(str(root.val))
        inorder(root.right, result)

# 4. BFS Level Order Traversal (Queue FIFO)
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(str(node.val))
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    return result

def main():
    root = None
    
    while True:
        print("\n--- BST & BFS Operations ---")
        print("1. Insert Numbers to BST ")
        print("2. Search a Value in BST (O(log N))")
        print("3. Inorder Traversal (Check if sorted!)")
        print("4. BFS Level Order Traversal (Level by Level)")
        print("5. Exit")
        
        choice = input("Choose Option (1-5): ").strip()
        
        if choice == "1":
            try:
                raw_input = input("Enter values to insert in BST: ")
                vals = [int(x) for x in raw_input.split()]
                for v in vals:
                    root = bst_insert(root, v)
                print(f"Added {len(vals)} nodes to BST! Root is {root.val}")
            except ValueError:
                print("Error: Please enter integers only.")
                
        elif choice == "2":
            if not root:
                print("BST is empty! Insert numbers first.")
            else:
                try:
                    target = int(input("Enter number to search: "))
                    found = bst_search(root, target)
                    if found:
                        print(f"🟢 Found {target} in BST!")
                    else:
                        print(f"🔴 {target} NOT found in BST.")
                except ValueError:
                    print("Error: Invalid number.")
                    
        elif choice == "3":
            if not root:
                print("BST is empty!")
            else:
                res = []
                inorder(root, res)
                print("Inorder (Sorted Ascending):", " -> ".join(res))
                
        elif choice == "4":
            if not root:
                print("BST is empty!")
            else:
                levels = level_order(root)
                print("Level Order (BFS) Traversal:")
                for idx, lvl in enumerate(levels):
                    print(f"  Level {idx}: [ " + ", ".join(lvl) + " ]")
                    
        elif choice == "5":
            print("done.")
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()

