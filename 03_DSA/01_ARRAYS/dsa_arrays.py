# 🐍 DSA Chapter 1: Array Reversal using Two-Pointer Approach

def reverse_array(arr):
    # Left pointer starting pointer index 0 par
    left = 0
    # Right pointer ending pointer index (length - 1) par
    right = len(arr) - 1
    
    print(f"Original Array: {arr}")
    
    # Loop tab tak chalega jab tak left pointer right se chota hai
    while left < right:
        print(f"Swapping elements: {arr[left]} (at index {left}) <-> {arr[right]} (at index {right})")
        
        # Pythonic swapping (No third variable needed!)
        arr[left], arr[right] = arr[right], arr[left]
        
        # Pointers ko center ki taraf badhana hai
        left += 0
        right -= 1
        
        print(f"Current State: {arr}\n")
    
    return arr

# Test run
my_list = [10, 20, 30, 40, 50]
reversed_list = reverse_array(my_list)
print(f"Final Reversed Array: {reversed_list}")

