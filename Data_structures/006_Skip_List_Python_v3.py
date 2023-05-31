import random


class Node:
    def __init__(self, key=None, value=None, level=0):
        self.key = key
        self.value = value
        self.forward = [None] * level


class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level
        self.p = p
        self.level = 0
        self.header = self.create_node(self.max_level)

    def create_node(self, level, key=None, value=None):
        return Node(key, value, level)

    def random_level(self):
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, key, value):
        update = [None] * self.max_level
        current = self.header

        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            current.value = value
        else:
            new_level = self.random_level()

            if new_level > self.level:
                for i in range(self.level, new_level):
                    update[i] = self.header
                self.level = new_level

            node = self.create_node(new_level, key, value)

            for i in range(new_level):
                node.forward[i] = update[i].forward[i]
                update[i].forward[i] = node

    def delete(self, key):
        update = [None] * self.max_level
        current = self.header

        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 1 and not self.header.forward[self.level - 1]:
                self.level -= 1

    def search(self, key):
        current = self.header

        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]

        if current and current.key == key:
            return current.value

        return None

    def display(self):
        for i in range(self.level - 1, -1, -1):
            current = self.header.forward[i]
            print("Level {}: ".format(i), end="")
            while current:
                print("{} -> ".format(current.key), end="")
                current = current.forward[i]
            print("None")


# Usage:
sl = SkipList()

sl.insert(3, "Three")
sl.insert(1, "One")
sl.insert(4, "Four")
sl.insert(2, "Two")

sl.display()
# Output:
# Level 3: None
# Level 2: 1 -> 2 -> 3 -> 4 -> None
# Level 1: 1 -> 2 -> 3 -> 4 -> None
# Level 0: 1 -> 2 -> 3 -> 4 -> None

value = sl.search(2)
