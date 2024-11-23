def is_palindrome(s):
    return s == s[::-1]

# Example usage:
s = input("Enter a string: ")
print(is_palindrome(s))
