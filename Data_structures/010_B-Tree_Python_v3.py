class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.child = []
        self.leaf = leaf

    def insert(self, key):
        if not self.child:
            self.insert_key(key)
        else:
            index = self.find_index(key)
            if self.child[index].is_full():
                self.split_child(index)
                if key > self.keys[index]:
                    index += 1
            self.child[index].insert(key)

    def insert_key(self, key):
        self.keys.append(key)
        self.keys.sort()

    def split_child(self, index):
        split_node = self.child[index]
        new_node = BTreeNode(leaf=split_node.leaf)
        self.child.insert(index + 1, new_node)
        self.keys.insert(index, split_node.keys.pop(len(split_node.keys) // 2))

        new_node.keys = split_node.keys[len(split_node.keys) // 2 + 1:]
        split_node.keys = split_node.keys[:len(split_node.keys) // 2]

        if not split_node.leaf:
            new_node.child = split_node.child[len(split_node.child) // 2:]
            split_node.child = split_node.child[:len(split_node.child) // 2]

    def find_index(self, key):
        for i in range(len(self.keys)):
            if key < self.keys[i]:
                return i
        return len(self.keys)

    def is_full(self):
        return len(self.keys) == 3


class BTree:
    def __init__(self):
        self.root = BTreeNode(leaf=True)

    def insert(self, key):
        if self.root.is_full():
            new_root = BTreeNode()
            new_root.child.append(self.root)
            self.root = new_root
            new_root.split_child(0)
        self.root.insert(key)

    def search(self, key):
        return self.root.search(key)

    def traverse(self):
        self.root.traverse()

    def print_tree(self):
        self.root.print_tree()


# Usage:
b_tree = BTree()
b_tree.insert(10)
b_tree.insert(20)
b_tree.insert(5)
b_tree.insert(15)
b_tree.insert(30)

print(b_tree.search(10))  # Output: True
print(b_tree.search(25))  # Output: False
