class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.value)
        result.extend(inorder_traversal(root.right))
    return result

def tree_sort(arr):
    root = None

    # Build BST
    for value in arr:
        root = insert(root, value)

    # Perform inorder traversal to get sorted elements
    sorted_arr = inorder_traversal(root)
    return sorted_arr

# Usage:
arr = [5, 3, 8, 4, 2]
sorted_arr = tree_sort(arr)
print(sorted_arr)
