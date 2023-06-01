class Node:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"Node({self.key}, {self.color})"

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, "black", None, None, None)
        self.root = self.nil

    def search(self, key, node=None):
        """Search for a key in the Red-Black Tree."""
        if node is None:
            node = self.root
        if node == self.nil or key == node.key:
            return node
        if key < node.key:
            return self.search(key, node.left)
        else:
            return self.search(key, node.right)

    def minimum(self, node=None):
        """Find the minimum key in the Red-Black Tree."""
        if node is None:
            node = self.root
        while node.left != self.nil:
            node = node.left
        return node

    def maximum(self, node=None):
        """Find the maximum key in the Red-Black Tree."""
        if node is None:
            node = self.root
        while node.right != self.nil:
            node = node.right
        return node

    def left_rotate(self, x):
        """Left rotate around node x."""
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        """Right rotate around node x."""
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        """Insert a key into the Red-Black Tree."""
        z = Node(key, "red", self.nil, self.nil, self.nil)
        y = self.
