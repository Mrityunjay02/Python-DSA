# Binary Tree DFS Traversals (Dynamic Keyboard Input)
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build Tree dynamically from level-order input using Queue (BFS)
def build_tree_from_list(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        curr = queue.popleft()
        
        # Left child
        if i < len(values):
            if values[i] is not None:
                curr.left = TreeNode(values[i])
                queue.append(curr.left)
            i += 1
            
        # Right child
        if i < len(values):
            if values[i] is not None:
                curr.right = TreeNode(values[i])
                queue.append(curr.right)
            i += 1
            
    return root

# 1. Inorder Traversal (Left -> Root -> Right)
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(str(root.val))
        inorder(root.right, result)

# 2. Preorder Traversal (Root -> Left -> Right)
def preorder(root, result):
    if root:
        result.append(str(root.val))
        preorder(root.left, result)
        preorder(root.right, result)

# 3. Postorder Traversal (Left -> Right -> Root)
def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(str(root.val))

def main():
    root = None
    
    while True:
        print("\n--- Binary Tree DFS Menu ---")
        print("1. Build / Change Tree")
        print("2. Inorder Traversal (Left -> Root -> Right)")
        print("3. Preorder Traversal (Root -> Left -> Right)")
        print("4. Postorder Traversal (Left -> Right -> Root)")
        print("5. Exit")
        
        choice = input("Choose Option (1-5): ").strip()
        
        if choice == "1":
            try:
                raw_input = input("Enter node values: ")
                vals = [int(x) if x.lower() != 'none' and x.lower() != 'null' else None for x in raw_input.split()]
                if vals:
                    root = build_tree_from_list(vals)
                    print(f"Tree built successfully with Root = {root.val}!")
                else:
                    print("Empty input. Tree not created.")
            except ValueError:
                print("Error: Please enter numbers only.")
                
        elif choice == "2":
            if not root:
                print("Tree is empty! Please build tree first (Option 1).")
            else:
                res = []
                inorder(root, res)
                print("Inorder (L -> Root -> R):", " -> ".join(res))
                
        elif choice == "3":
            if not root:
                print("Tree is empty! Please build tree first (Option 1).")
            else:
                res = []
                preorder(root, res)
                print("Preorder (Root -> L -> R):", " -> ".join(res))
                
        elif choice == "4":
            if not root:
                print("Tree is empty! Please build tree first (Option 1).")
            else:
                res = []
                postorder(root, res)
                print("Postorder (L -> R -> Root):", " -> ".join(res))
                
        elif choice == "5":
            print("done.")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()
