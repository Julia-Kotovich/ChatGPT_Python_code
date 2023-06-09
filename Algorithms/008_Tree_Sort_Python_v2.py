class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    return node

def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.value)
        inorder_traversal(node.right, result)

def tree_sort(arr):
    root = None

    # Build BST
    for value in arr:
        root = insert(root, value)

    result = []
    # Perform inorder traversal to get sorted elements
    inorder_traversal(root, result)

    return result

# Usage:
arr = [5, 3, 8, 4, 2]
sorted_arr = tree_sort(arr)
print(sorted_arr)
