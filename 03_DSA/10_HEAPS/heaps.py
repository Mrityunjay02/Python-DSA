# Heaps & Priority Queues (heapq module demo)
import heapq

def test_min_heap():
    heap = []
    while True:
        print("\n--- Min-Heap Menu ---")
        print(f"Current Heap Array: {heap}")
        print(f"Current Minimum (heap[0]): {heap[0] if heap else 'Empty'}")
        print("1. Push elements (space-separated)")
        print("2. Pop Minimum (heappop)")
        print("3. Back to Main")
        
        choice = input("Choose Option (1-3): ").strip()
        
        if choice == "1":
            try:
                raw = input("Enter numbers to push: ")
                vals = [int(x) for x in raw.split()]
                for v in vals:
                    heapq.heappush(heap, v)
                print(f"Updated Heap: {heap} | Min is {heap[0]}")
            except ValueError:
                print("Error: Please enter integers only.")
                
        elif choice == "2":
            if heap:
                min_val = heapq.heappop(heap)
                print(f"🟢 Popped Smallest Element: {min_val}")
            else:
                print("Heap is empty!")
                
        elif choice == "3":
            break
        else:
            print("Invalid Choice.")

def test_max_heap():
    max_heap = []  # Stores negative values
    while True:
        # Convert internal negative numbers to positive for visual display
        actual_values = [-x for x in max_heap]
        print("\n--- Max-Heap Menu ---")
        print(f"Current Max-Heap Elements: {actual_values}")
        print(f"Current Maximum: {actual_values[0] if actual_values else 'Empty'}")
        print("1. Push elements (space-separated)")
        print("2. Pop Maximum")
        print("3. Back to Main")
        
        choice = input("Choose Option (1-3): ").strip()
        
        if choice == "1":
            try:
                raw = input("Enter numbers to push: ")
                vals = [int(x) for x in raw.split()]
                for v in vals:
                    heapq.heappush(max_heap, -v)  # store negative
                print(f"Updated Max-Heap: {[-x for x in max_heap]} | Max is {-max_heap[0]}")
            except ValueError:
                print("Error: Please enter integers only.")
                
        elif choice == "2":
            if max_heap:
                max_val = -heapq.heappop(max_heap)
                print(f"🟢 Popped Largest Element: {max_val}")
            else:
                print("Max-Heap is empty!")
                
        elif choice == "3":
            break
        else:
            print("Invalid Choice.")

def test_kth_largest():
    print("\n--- Find K-th Largest Element (O(N log K)) ---")
    try:
        raw = input("Enter array of numbers : ")
        nums = [int(x) for x in raw.split()]
        k = int(input("Enter K (e.g. 2 for 2nd largest): "))
        
        if k < 1 or k > len(nums):
            print("Invalid K value!")
            return
            
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        print(f"🟢 The {k}-th Largest Element in {nums} is: {min_heap[0]}")
    except ValueError:
        print("Error: Invalid inputs.")

def main():
    while True:
        print("\n=== Heaps & Priority Queues Menu ===")
        print("1. Test Min-Heap (Default Python)")
        print("2. Test Max-Heap (Negative values trick)")
        print("3. Solve K-th Largest Element Problem")
        print("4. Exit")
        
        choice = input("Choose Option (1-4): ").strip()
        
        if choice == "1":
            test_min_heap()
        elif choice == "2":
            test_max_heap()
        elif choice == "3":
            test_kth_largest()
        elif choice == "4":
            print("done.")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()

