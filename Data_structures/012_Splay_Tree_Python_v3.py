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
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
            node = self._rotate_right(node)
        elif key > node.key:
            node.right = self._insert(node.right, key)
            node = self._rotate_left(node)
        
        return node

    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.key == key

    def _splay(self, node, key):
        if node is None or node.key == key:
            return node
        
        if key < node.key:
            if node.left is None:
                return node
            if key < node.left.key:
                node.left.left = self._splay(node.left.left, key)
                node = self._rotate_right(node)
            elif key > node.left.key:
                node.left.right = self._splay(node.left.right, key)
                if node.left.right is not None:
                    node.left = self._rotate_left(node.left)
            if node.left is not None:
                node = self._rotate_right(node)
            return node

        else:
            if node.right is None:
                return node
            if key < node.right.key:
                node.right.left = self._splay(node.right.left, key)
                if node.right.left is not None:
                    node.right = self._rotate_right(node.right)
            elif key > node.right.key:
                node.right.right = self._splay(node.right.right, key)
                node = self._rotate_left(node)
            if node.right is not None:
                node = self._rotate_left(node)
            return node

    def _rotate_left(self, node):
        child = node.right
        node.right = child.left
        if child.left is not None:
            child.left.parent = node
        child.parent = node.parent
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        if child.left is not None:
            child.left.parent = node
        child.left = node
        node.parent = child
        return child

    def _rotate_right(self, node):
        child = node.left
        node.left = child.right
        if child.right is not None:
            child.right.parent = node
        child.parent = node.parent
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        if child.right is not None:
            child.right.parent = node
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
