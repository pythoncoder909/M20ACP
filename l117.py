# Calculate and print the product of the tuples
print(f"The product of tup1 is: {multiply_tuple_elements(tup1)}")
print(f"The product of tup2 is: {multiply_tuple_elements(tup2)}")

# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test dictionary:", test_dict)

# Ask the user to enter a value
value_to_check = int(input("Enter the value to check its frequency in the dictionary: "))

# Check the frequency of the entered value
frequency = list(test_dict.values()).count(value_to_check)

# Print the result
print(f"The frequency of the value {value_to_check} is: {frequency}")

