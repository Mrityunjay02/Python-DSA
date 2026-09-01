# Hashing & Dictionaries Playground (Interactive Session)

# 1. Frequency Counter (using .get() to avoid KeyError)
def frequency_counter(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# 2. Two Sum Problem - Optimized using Hash Map O(N)
def two_sum(nums, target):
    # key: number, value: index
    seen = {}
    
    for idx, num in enumerate(nums):
        complement = target - num
        # O(1) average lookup in hash map
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
        
    return []

def main():
    while True:
        print("\n--- Hashing Algorithms Menu ---")
        print("1. Character Frequency Counter")
        print("2. Two Sum (Find indices of sum)")
        print("3. Exit")
        
        choice = input("Select Option (1-3): ").strip()
        
        if choice == "1":
            text = input("Enter a string: ")
            print("Frequencies:", frequency_counter(text))
            
        elif choice == "2":
            try:
                nums = [int(x) for x in input("Enter numbers (spaces): ").split()]
                target = int(input("Enter target sum: "))
                result = two_sum(nums, target)
                if result:
                    print(f"Indices found: {result} (Values: {nums[result[0]]} + {nums[result[1]]} = {target})")
                else:
                    print("No two numbers sum up to the target.")
            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")
                
        elif choice == "3":
            print("Bye-bye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

