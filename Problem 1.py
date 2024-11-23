def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

# Example usage:
n = int(input("Enter an integer: "))
print(is_prime(n))
