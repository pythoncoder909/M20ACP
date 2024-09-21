def find_symmetric_difference(set1, set2):
    # Find and return the symmetric difference
    return set1.symmetric_difference(set2)

# Example sets for part A
set1_a = {'blue', 'green'}
set2_a = {'blue', 'yellow'}

# Example sets for part B
set1_b = {1, 2, 3, 4, 5}
set2_b = {1, 5, 6, 7, 8, 9}

# Find symmetric differences
sym_diff_a = find_symmetric_difference(set1_a, set2_a)
sym_diff_b = find_symmetric_difference(set1_b, set2_b)

# Print the results
print(f"Symmetric Difference of Set A: {sym_diff_a}")
print(f"Symmetric Difference of Set B: {sym_diff_b}")

