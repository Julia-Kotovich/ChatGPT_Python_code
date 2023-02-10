# Creating an empty dictionary
hash_table = {}

# Adding key-value pairs to the dictionary
hash_table["John"] = 25
hash_table["Jane"] = 22
hash_table["Jim"] = 30

# Retrieving the value associated with a key
print("John's age is: ", hash_table["John"])
print("Jane's age is: ", hash_table["Jane"])
print("Jim's age is: ", hash_table["Jim"])

# Updating a value associated with a key
hash_table["John"] = 28
print("John's updated age is: ", hash_table["John"])

# Removing a key-value pair from the dictionary
del hash_table["Jim"]
print("Jim's age is not in the table: ", "Jim" in hash_table)
