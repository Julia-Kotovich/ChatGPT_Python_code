class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def in_order_traversal(root, arr):
    if root:
        in_order_traversal(root.left, arr)
        arr.append(root.data)
        in_order_traversal(root.right, arr)

def tree_sort(arr):
    n = len(arr)
    root = None
    for i in range(n):
        node = Node(arr[i])
        insert(root, node)
    sorted_arr = []
    in_order_traversal(root, sorted_arr)
    return sorted_arr
