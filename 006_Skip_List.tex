import random

class Node:
    def __init__(self, data, level):
        self.data = data
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.header = self.create_node(self.max_level, -1)

    def create_node(self, level, data):
        return Node(data, level)

    def random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def search(self, search_value):
        x = self.header
        for i in range(self.max_level, -1, -1):
            while x.forward[i] and x.forward[i].data < search_value:
                x = x.forward[i]
        x = x.forward[0]
        if x and x.data == search_value:
            return x
        else:
            return None

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        x = self.header
        for i in range(self.max_level, -1, -1):
            while x.forward[i] and x.forward[i].data < value:
                x = x.forward[i]
            update[i] = x
        x = x.forward[0]
        if x == None or x.data != value:
            rlevel = self.random_level()
            if rlevel > self.max_level:
                for i in range(self.max_level + 1, rlevel + 1):
                    update[i] = self.header
                self.max_level = rlevel
            x = self.create_node(rlevel, value)
            for i in range(rlevel + 1):
                x.forward[i] = update[i].forward[i]
                update[i].forward[i] = x

# Driver code
skip_list = SkipList(3, 0.5)
skip_list.insert(1)
skip_list.insert(2)
skip_list.insert(3)
skip_list.insert(4)
result = skip_list.search(3)
if result:
    print("Found", result.data)
else:
    print("Not found")
