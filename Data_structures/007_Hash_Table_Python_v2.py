class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = Node(key, value)

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError("Key not found in hash table")

    def remove(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return
            previous = current
            current = current.next
        raise KeyError("Key not found in hash table")

    def display(self):
        for index in range(self.size):
            current = self.table[index]
            print(f"Index {index}: ", end="")
            while current:
                print(f"{current.key}={current.value} -> ", end="")
                current = current.next
            print("None")


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
# Index 0: None
# Index 1: None
# Index 2: apple=5 -> orange=8 -> None
# Index 3: None
# Index 4: None
# Index 5: None
# Index 6: None
# Index 7: None
# Index 8: None
# Index 9: None
