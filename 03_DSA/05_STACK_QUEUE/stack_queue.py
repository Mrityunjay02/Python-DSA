# Stack and Queue Operations Demo
from collections import deque

def test_stack():
    stack = []
    while True:
        print("\n--- Stack Menu (LIFO) ---")
        print(f"Current Stack: {stack}")
        print("1. Push (Add to Top)")
        print("2. Pop (Remove from Top)")
        print("3. Peek (Check Top)")
        print("4. Back to Main")
        
        choice = input("Option (1-4): ").strip()
        
        if choice == "1":
            try:
                raw_input = input("Enter values to push (spaces for multiple): ")
                vals = [int(x) for x in raw_input.split()]
                for val in vals:
                    stack.append(val)  # append is O(1)
            except ValueError:
                print("Error: Please enter integers only.")
                
        elif choice == "2":
            if stack:
                val = stack.pop()  # pop is O(1)
                print(f"Popped value: {val}")
            else:
                print("Stack is empty!")
                
        elif choice == "3":
            if stack:
                print(f"Top element (Peek): {stack[-1]}")
            else:
                print("Stack is empty!")
                
        elif choice == "4":
            break
        else:
            print("Invalid option.")

def test_queue():
    queue = deque()
    while True:
        print("\n--- Queue Menu (FIFO) ---")
        print(f"Current Queue: {list(queue)}")
        print("1. Enqueue (Add to Rear)")
        print("2. Dequeue (Remove from Front)")
        print("3. Back to Main")
        
        choice = input("Option (1-3): ").strip()
        
        if choice == "1":
            try:
                raw_input = input("Enter values to enqueue (spaces for multiple): ")
                vals = [int(x) for x in raw_input.split()]
                for val in vals:
                    queue.append(val)  # append is O(1)
            except ValueError:
                print("Error: Please enter integers only.")
                
        elif choice == "2":
            if queue:
                val = queue.popleft()  # popleft is O(1) in deque!
                print(f"Dequeued value: {val}")
            else:
                print("Queue is empty!")
                
        elif choice == "3":
            break
        else:
            print("Invalid option.")

def main():
    while True:
        print("\n=== Linear Data Structures ===")
        print("1. Test Stack (LIFO)")
        print("2. Test Queue (FIFO)")
        print("3. Exit")
        
        choice = input("Choose Structure (1-3): ").strip()
        
        if choice == "1":
            test_stack()
        elif choice == "2":
            test_queue()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

