class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.splay(key)
            if key < self.root.key:
                new_node = Node(key)
                new_node.left = self.root.left
                new_node.right = self.root
                self.root.left = None
                self.root = new_node
            elif key > self.root.key:
                new_node = Node(key)
                new_node.right = self.root.right
                new_node.left = self.root
                self.root.right = None
                self.root = new_node

    def search(self, key):
        if self.root is None:
            return False
        else:
            self.splay(key)
            return self.root.key == key

    def splay(self, key):
        if self.root is None or self.root.key == key:
            return

        dummy = Node(None)
        left = right = dummy
        current = self.root

        while True:
            if key < current.key:
                if current.left is None:
                    break
                if key < current.left.key:
                    current = self.rotate_right(current)
                    if current.left is None:
                        break
                right.left = current
                right = current
                current = current.left
            elif key > current.key:
                if current.right is None:
                    break
                if key > current.right.key:
                    current = self.rotate_left(current)
                    if current.right is None:
                        break
                left.right = current
                left = current
                current = current.right
            else:
                break

        left.right = current.left
        right.left = current.right
        current.left = dummy.right
        current.right = dummy.left
        self.root = current

    def rotate_left(self, node):
        child = node.right
        node.right = child.left
        if child.left is not None:
            child.left.parent = node
        child.parent = node.parent
        if node.parent is None:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        child.left = node
        node.parent = child
        return child

    def rotate_right(self, node):
        child = node.left
        node.left = child.right
        if child.right is not None:
            child.right.parent = node
        child.parent = node.parent
        if node.parent is None:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        child.right = node
        node.parent = child
        return child


# Usage:
splay_tree = SplayTree()
splay_tree.insert(10)
splay_tree.insert(20)
splay_tree.insert(5)
splay_tree.insert(15)
splay_tree.insert(30)

print(splay_tree.search(10))  # Output: True
print(splay_tree.search(25))  # Output: False
