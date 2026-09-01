# String Algorithms Playground (Interactive Session)

# 1. Reverse String using Two-Pointer (Mutable list trick)
def reverse_string(s):
    # strings are immutable, convert to list of chars first
    chars = list(s)
    
    left = 0
    right = len(chars) - 1
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
        
    # join list back to string
    return "".join(chars)

# 2. Palindrome Check (Two-Pointer)
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# 3. Anagram Check (Sorting Method)
def is_anagram(s1, s2):
    # remove spaces and lower case
    s1_clean = s1.replace(" ", "").lower()
    s2_clean = s2.replace(" ", "").lower()
    
    return sorted(s1_clean) == sorted(s2_clean)

# Main Execution Loop
def main():
    while True:
        print("\n--- String Algorithms Menu ---")
        print("1. Reverse a String")
        print("2. Check Palindrome")
        print("3. Check Anagram")
        print("4. Exit")
        
        choice = input("Select Option (1-4): ").strip()
        
        if choice == "1":
            word = input("Enter string to reverse: ")
            print("Reversed:", reverse_string(word))
            
        elif choice == "2":
            word = input("Enter string to check: ")
            if is_palindrome(word):
                print(f"Yes, '{word}' is a Palindrome!")
            else:
                print(f"No, '{word}' is not a Palindrome.")
                
        elif choice == "3":
            str1 = input("Enter first string: ")
            str2 = input("Enter second string: ")
            if is_anagram(str1, str2):
                print(f"Yes, '{str1}' and '{str2}' are Anagrams!")
            else:
                print(f"No, '{str1}' and '{str2}' are not Anagrams.")
                
        elif choice == "4":
            print("done")
            break
        else:
            print("Invalid Option, try again.")

if __name__ == "__main__":
    main()

