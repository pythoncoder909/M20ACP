def separate_odd_even_squares(start, end):
    # Generate a list of square values within the specified range
    square_values = [x**2 for x in range(start, end + 1)]
    
    # Separate odd and even square values
    odd_squares = [x for x in square_values if x % 2 != 0]
    even_squares = [x for x in square_values if x % 2 == 0]
    
    # Print the results
    print(f"Odd squares: {odd_squares}")
    print(f"Even squares: {even_squares}")

# Example usage:
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

separate_odd_even_squares(start_range, end_range)


