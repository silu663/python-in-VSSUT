#  solution for the basic datastructure and tuples

# 1. Accessing the elements present in a list
list_num = [5, 9, 10, 15, 32]
print(list_num)  # [5, 9, 10, 15, 32]

# 2. Accessing elements according to their index
print(list_num[0])  # 5

# 3. Print a range of values according to specified indexes
print(list_num[1:4])  # [9, 10, 15]

# 4. Print the length of the list
print(len(list_num))  # 5

# 5. Replacing the value specifying an index
list_num[2] = 100
print(list_num)  # [5, 9, 100, 15, 32]

# 6. Insert an element
list_num.insert(3, 60)
print(list_num)  # [5, 9, 100, 60, 15, 32]

# 7. Insert a value at the end
list_num = [5, 9, 10, 15, 32]
list_num.append(55)
print(list_num)  # [5, 9, 10, 15, 32, 55]

# 8. Performing Max - Min functions
list_num = [5, 9, 10, 15, 32]
print(max(list_num))  # 32
print(min(list_num))  # 5

# 9. Sorting
list_num = [5, 9, 14, 12, 2]
list_num.sort()
print(list_num)  # [2, 5, 9, 12, 14]

# 10. Cloning of list
list_num = [1, 2, 3, 4, 5]
list_val = list_num
print(list_val)  # [1, 2, 3, 4, 5]

# 11. Extending list
list_num = [5, 9, 10, 15, 32]
list_var = [3, 7, 39]
list_num.extend(list_var)
print(list_num)  # [5, 9, 10, 15, 32, 3, 7, 39]

# 12. Reversing list
list1 = [3, 7, 39]
list1.reverse()
print(list1)  # [39, 7, 3]

# 1. Tuple length
thisTuple = ("Apple", "Banana", "Cherry")
print(len(thisTuple))  # Output: 3

# 2. Adding elements of two tuples (concatenation)
tuple1 = (2, 4, 6, 8, 10)
tuple2 = (3, 8, 10, 19)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (2, 4, 6, 8, 10, 3, 8, 10, 19)

# 3. Performing Max function
tuple3 = (2, 4, 6, 8, 10, 3, 8, 10, 19)
print(max(tuple3))  # Output: 19

# 1. Performing Min function
tuple3 = (2, 4, 6, 8, 10, 3, 8, 10, 19)
print(min(tuple3))  # Output: 2

# 2. Performing Boolean functions on Tuples
tuple1 = (2, 4, 6, 8, 10)
tuple2 = (3, 8, 10, 19)

print(tuple1 < tuple2)   # Output: True
print(tuple1 > tuple2)   # Output: False
print(tuple1 == tuple2)  # Output: False (note: in your notes it showed True, but actually these tuples differ)

# 3. Duplication in Tuples
tuple1 = (2, 4, 6, 8, 10)
tuple4 = tuple1 * 2
print(tuple4)  # Output: (2, 4, 6, 8, 10, 2, 4, 6, 8, 10)

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