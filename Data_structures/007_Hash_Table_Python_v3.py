class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        raise KeyError("Key not found in hash table")

    def remove(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.rehash()
                return
            index = (index + 1) % self.size

        raise KeyError("Key not found in hash table")

    def rehash(self):
        new_keys = [None] * self.size
        new_values = [None] * self.size

        for key, value in zip(self.keys, self.values):
            if key is not None:
                index = self.hash_function(key)
                while new_keys[index] is not None:
                    index = (index + 1) % self.size
                new_keys[index] = key
                new_values[index] = value

        self.keys = new_keys
        self.values = new_values

    def display(self):
        for index in range(self.size):
            if self.keys[index] is not None:
                print(f"Index {index}: {self.keys[index]}={self.values[index]}")
            else:
                print(f"Index {index}: None")


# Usage:
hash_table = HashTable(10)

hash_table.insert("apple", 3)
hash_table.insert("banana", 6)
hash_table.insert("orange", 8)
hash_table.insert("apple", 5)

print(hash_table.get("apple"))  # Output: 5

hash_table.remove("banana")

hash_table.display()
# Output:
# Index 0: apple=5
# Index 1: None
# Index 2: orange=8
# Index 3: None
# Index 4: None
# Index 5: None
# Index 6: None
# Index 7: None
# Index 8: None
# Index 9: None
