# Array Algorithms

# Helper function to reverse part of list (useful for rotation)
def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# 1. Array Rotation (using 3-step reversal)
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # handles cases where k is greater than array length
    
    # step 1: reverse complete array
    reverse(arr, 0, n - 1)
    # step 2: reverse first k elements
    reverse(arr, 0, k - 1)
    # step 3: reverse the rest
    reverse(arr, k, n - 1)
    
    return arr

# 2. Sliding Window (Max sum subarray of size K)
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        print("Error: Window size is greater than array size")
        return -1
        
    # sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # slide the window forward
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

# 3. Prefix Sum (Range Sum Query)
def range_sum(arr, left, right):
    n = len(arr)
    
    # build prefix array
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
        
    # sum from left to right index
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left-1]

# 4. Kadane's Algorithm (Max contiguous subarray sum)
def kadanes(arr):
    max_so_far = arr[0]
    curr_max = arr[0]
    
    for val in arr[1:]:
        curr_max = max(val, curr_max + val)
        max_so_far = max(max_so_far, curr_max)
        
    return max_so_far

# 5. Dutch National Flag (Sort 0s, 1s, and 2s in one pass)
def sort_012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            
    return arr

# Interactive Driver code
def main():
    while True:
        print("\n--- Array Playground Menu ---")
        print("1. Array Rotation")
        print("2. Sliding Window (Max sum subarray)")
        print("3. Prefix Sum Query")
        print("4. Kadane's Algorithm")
        print("5. Dutch National Flag (Sort 0,1,2)")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            nums = [int(x) for x in input("Enter array (spaces): ").split()]
            k = int(input("Steps: "))
            print("Result:", rotate_array(nums, k))
            
        elif choice == "2":
            nums = [int(x) for x in input("Enter array (spaces): ").split()]
            k = int(input("Window size: "))
            print("Result:", max_sum_subarray(nums, k))
            
        elif choice == "3":
            nums = [int(x) for x in input("Enter array (spaces): ").split()]
            l = int(input("Left Index: "))
            r = int(input("Right Index: "))
            print("Result:", range_sum(nums, l, r))
            
        elif choice == "4":
            nums = [int(x) for x in input("Enter array (spaces): ").split()]
            print("Result:", kadanes(nums))
            
        elif choice == "5":
            nums = [int(x) for x in input("Enter array of 0,1,2 (spaces): ").split()]
            print("Result:", sort_012(nums))
            
        elif choice == "6":
            print("done")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
