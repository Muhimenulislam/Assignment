def count_digits(s):
    count = sum(char.isdigit() for char in s)
    print(f"Total digits are: {count}")

# Example usage:
s = input("Enter a string: ")
count_digits(s)
