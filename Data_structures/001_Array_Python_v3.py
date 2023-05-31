import array as arr

# Create an array of floats
my_array = arr.array('f', [1.5, 2.3, 3.7, 4.1, 5.9])

# Access elements in the array
print(my_array[0])  # Output: 1.5
print(my_array[3])  # Output: 4.1

# Modify an element in the array
my_array[2] = 10.2

# Access the modified element
print(my_array[2])  # Output: 10.2

# Append elements to the array
my_array.append(6.4)
my_array.extend([7.8, 8.6, 9.1])

# Print all elements in the array
for num in my_array:
    print(num)

# Get the length of the array
print(len(my_array))  # Output: 9
