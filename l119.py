# Take user input
n = int(input("Enter a number: "))

# List of odd numbers less than the input value
odd_numbers = [x for x in range(n) if x % 2 != 0]

# List of even numbers less than the input value
even_numbers = [x for x in range(n) if x % 2 == 0]

# Print the results
print(f"Odd numbers under {n}: {odd_numbers}")
print(f"Even numbers under {n}: {even_numbers}")

