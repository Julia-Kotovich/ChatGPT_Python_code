import random

class Node:
    def __init__(self, data=None, height=1):
        self.data = data
        self.forward = [None] * height

class SkipList:
    MAX_HEIGHT = 16
    P = 0.5

    def __init__(self):
        self.head = Node()
        self.height = 1

    def _random_height(self):
        height = 1
        while random.random() < self.P and height < self.MAX_HEIGHT:
            height += 1
        return height

    def insert(self, data):
        new_node = Node(data, self._random_height())
        current = self.head
        update = [None] * self.height

        for i in range(self.height - 1, -1, -1):
            while current.forward[i] and current.forward[i].data < data:
                current = current.forward[i]
            update[i] = current

        for i in range(new_node.height):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

        if new_node.height > self.height:
            self.height = new_node.height

    def search(self, target):
        current = self.head
        for i in range(self.height - 1, -1, -1):
            while current.forward[i] and current.forward[i].data < target:
                current = current.forward[i]

        current = current.forward[0]

        if current and current.data == target:
            return True
        else:
            return False

    def delete(self, target):
        current = self.head
        update = [None] * self.height

        for i in range(self.height - 1, -1, -1):
            while current.forward[i] and current.forward[i].data < target:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.data == target:
            for i in range(self.height):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.height > 1 and self.head.forward[self.height - 1] is None:
                self.height -= 1

            return True
        else:
            return False

    def display(self):
        for i in range(self.height - 1, -1, -1):
            current = self.head.forward[i]
            print("Level {}: ".format(i + 1), end="")
            while current:
                print(current.data, end=" -> ")
                current = current.forward[i]
            print("None")


# Usage:
sl = SkipList()

sl.insert(10)
sl.insert(5)
sl.insert(15)
sl.insert(20)
sl.insert(7)

sl.display()
# Output:
# Level 5: None
# Level 4: None
# Level 3: None
# Level 2: 5 -> 7 -> 15 -> 20 -> None
# Level 1: 5 -> 7 -> 10 -> 15 -> 20 -> None

print(sl.search(15))  # True
print(sl.search(8))   # False

sl.delete(10)

sl.display()
# Output:
# Level 5: None
# Level 4: None
# Level 3: None
# Level 2: 5 -> 7 -> 15 -> 20 -> None
# Level 1: 5 -> 7 -> 15 -> 20 -> None
