import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Access elements in the array
print(my_array[0])  # Output: 1
print(my_array[3])  # Output: 4

# Modify an element in the array
my_array[2] = 10

# Access the modified element
print(my_array[2])  # Output: 10

# Append elements to the array
my_array.append(6)
my_array.extend([7, 8, 9])

# Print all elements in the array
for num in my_array:
    print(num)

# Get the length of the array
print(len(my_array))  # Output: 9
