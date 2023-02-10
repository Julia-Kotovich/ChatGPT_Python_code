class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        if self.root:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif data < node.data and node.left:
            return self._find(data, node.left)
        elif data > node.data and node.right:
            return self._find(data, node.right)

    def delete(self, data):
        if self.root:
            self.root = self._delete(data, self.root)

    def _delete(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left = self._delete(data, node.left)
        elif data > node.data:
            node.right = self._delete(data, node.right)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_val = self.find_min(node.right)
            node.data = min_val
            node.right = self._delete(min_val, node.right)
        return node

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current.data

bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Finding 6: ", bst.find(6))
print("Finding 10: ", bst.find(10))

bst.delete(3)
print("Finding 3: ", bst.find(3))
