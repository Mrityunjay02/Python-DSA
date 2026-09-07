# Heap Core Problems (Top K Frequent, K-th Smallest, Merge K Sorted)
import heapq
from collections import Counter

# 1. Top K Frequent Elements (O(N log K))
def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for freq, num in heap]

# 2. K-th Smallest Element in Array (O(N log K))
def find_kth_smallest(nums, k):
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]

# 3. Merge K Sorted Arrays (O(N log K))
def merge_k_sorted(arrays):
    heap = []
    # Push first element of each array: (val, array_idx, elem_idx)
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
            
    result = []
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # If there is a next element in the same array, push it
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
            
    return result

def main():
    while True:
        print("\n=== Heap Core Problems Menu ===")
        print("1. Top K Frequent Elements (LeetCode 347)")
        print("2. Find K-th Smallest Element")
        print("3. Merge K Sorted Arrays (LeetCode 23 style)")
        print("4. Exit")
        
        choice = input("Choose Option (1-4): ").strip()
        
        if choice == "1":
            try:
                raw = input("Enter array (e.g. 1 1 1 2 2 3): ")
                nums = [int(x) for x in raw.split()]
                k = int(input("Enter K (e.g. 2): "))
                
                res = top_k_frequent(nums, k)
                print(f"🟢 Top {k} Frequent Elements in {nums}: {res}")
            except Exception as e:
                print("Error: Invalid inputs.", e)
                
        elif choice == "2":
            try:
                raw = input("Enter array (e.g. 7 10 4 3 20 15): ")
                nums = [int(x) for x in raw.split()]
                k = int(input("Enter K (e.g. 3 for 3rd smallest): "))
                
                if k < 1 or k > len(nums):
                    print("Error: K is out of range!")
                else:
                    ans = find_kth_smallest(nums, k)
                    print(f"🟢 The {k}-th Smallest Element in {nums} is: {ans}")
            except ValueError:
                print("Error: Please enter numbers only.")
                
        elif choice == "3":
            try:
                k = int(input("How many sorted arrays to merge? (e.g. 3): "))
                arrays = []
                for i in range(k):
                    raw = input(f"  Enter sorted array {i+1} (spaces): ")
                    arrays.append([int(x) for x in raw.split()])
                    
                merged = merge_k_sorted(arrays)
                print(f"🟢 Merged Single Sorted Array: {merged}")
            except Exception as e:
                print("Error:", e)
                
        elif choice == "4":
            print("Keep rockin the 90-Day Challenge! Bye.")
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()

