class Node:
    def __init__(self, key, left=None, right=None, height=1):
        self.key = key
        self.left = left
        self.right = right
        self.height = height
    
    def __repr__(self):
        return f"Node({self.key})"

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        """Get the height of a node."""
        return node.height if node else 0

    def balance_factor(self, node):
        """Get the balance factor of a node."""
        return self.height(node.right) - self.height(node.left)

    def left_rotate(self, x):
        """Left rotate around node x."""
        y = x.right
        x.right = y.left
        y.left = x
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def right_rotate(self, x):
        """Right rotate around node x."""
        y = x.left
        x.left = y.right
        y.right = x
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, key):
        """Insert a key into the AVL Tree."""
        def insert_node(node):
            if not node:
                return Node(key)
            if key < node.key:
                node.left = insert_node(node.left)
            else:
                node.right = insert_node(node.right)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
            balance = self.balance_factor(node)
            if balance > 1 and key < node.right.key:
                return self.left_rotate(node)
            if balance < -1 and key > node.left.key:
                return self.right_rotate(node)
            if balance > 1 and key > node.right.key:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
            if balance < -1 and key < node.left.key:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
            return node
        self.root = insert_node(self.root)
