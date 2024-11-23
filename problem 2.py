def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage:
n = int(input("Enter an integer: "))
multiplication_table(n)
