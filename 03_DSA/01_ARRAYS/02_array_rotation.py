# 🐍 DSA Chapter 1: Array Rotation by K Steps (Interactive Execution)

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Modulo calculation
    
    print(f"\n[Step 0] Original Array: {arr} | Rotating right by k={k} steps")
    
    # 1. Reverse entire array
    reverse(arr, 0, n - 1)
    print(f"[Step 1] After entire array reverse: {arr}")
    
    # 2. Reverse first k elements
    reverse(arr, 0, k - 1)
    print(f"[Step 2] After reversing first {k} elements: {arr}")
    
    # 3. Reverse remaining n-k elements
    reverse(arr, k, n - 1)
    print(f"[Step 3] After reversing remaining {n - k} elements (Final Rotated): {arr}")
    
    return arr

# Interactive Keyboard Inputs
try:
    user_array_input = input("Enter array elements separated by spaces (e.g. 1 2 3 4 5): ")
    my_list = [int(x) for x in user_array_input.split()]
    
    k_input = int(input("Enter number of steps to rotate (k): "))
    
    # Run logic
    rotate_array(my_list, k_input)
except ValueError:
    print("❌ Error: Invalid input! Please enter only space-separated integers for array and an integer for k.")

