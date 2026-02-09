# Experiment A: Demonstrate basic list operations

list_num = [5, 9, 10, 15, 32]

# Print the elements in the list
print(list_num)

# Print element by index
print(list_num[1])  # Output: 9

# Print a slice of values according to given index
print(list_num[1:4])  # Output: [9, 10, 15]

# Print the length of the list
print(len(list_num))  # Output: 5

# Replace a value at a given index
list_num[2] = 100
print(list_num)  # Output: [5, 9, 100, 15, 32]

# Insert a number after index 3
list_num.insert(3, 60)
print(list_num)  # Output: [5, 9, 100, 60, 15, 32]

# Append a number at the end
list_num.append(55)
print(list_num)  # Output: [5, 9, 100, 60, 15, 32, 55]

# Maximum and minimum values
print(max(list_num))  # Output: 100
print(min(list_num))  # Output: 5

# Sorting the list
list_num.sort()
print(list_num)  # Output: [5, 9, 15, 32, 55, 60, 100]

# Cloning the list
list_val = list_num
print(list_val)

# Extending the list
list_var = [3, 7, 9]
list_num.extend(list_var)
print(list_num)  # Output: [5, 9, 15, 32, 55, 60, 100, 3, 7, 9]