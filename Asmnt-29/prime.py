# List comprehension to generate prime numbers less than 500
prime_numbers = [num for num in range(2, 500) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]

# Print the list of prime numbers
print(prime_numbers)
