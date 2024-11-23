def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels: {count}")

# Example usage
count_vowels("hello")
