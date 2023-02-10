class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.key})"

class SplayTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        """Search for a key in the Splay Tree."""
        node = self.root
        while node is not None:
            if node.key == key:
                break
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        return node

    def left_rotate(self, x):
        """Left rotate around node x."""
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def right_rotate(self, x):
        """Right rotate around node x."""
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def splay(self, node):
        """Splay node to the root of the Splay Tree."""
        while node.parent is not None:
            if node.parent.parent is None:
                if node.parent.left == node:
                    self.root = self.right_rotate(node.parent)
                else:
                    self.root = self.left_rotate(node.parent)
                break
            elif node.parent.left == node and node.parent.parent.left == node.parent:
                self.root = self.right_rotate(node.parent.parent)
                self.root = self.right_rotate(node.parent)
            elif node.parent.right == node and node.parent.parent.right == node.parent:
                self.root = self.left_rotate(node.parent.parent)
                self.root = self.left_rotate(node.parent)
            elif node.parent.left == node and node.parent.parent.right == node.parent:
                self.root = self.right_rotate(node.parent)
                self.root = self.left_rotate(node.parent)
            else:
                self.root = self.left_rotate(node.parent)
                self.root = self.right_rotate(node.parent)
        return self.root

    def insert(self, key):
        """Insert a key into the Splay Tree."""
        node = Node(key)
        if self.root is None:
            self.root = node
            return
        self.root = self.splay(self.search(key))
        if self.root.key
