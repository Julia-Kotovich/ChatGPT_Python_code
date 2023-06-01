class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def build_cartesian_tree(arr):
    if not arr:
        return None

    root_index = find_max_index(arr)
    root = Node(arr[root_index])

    root.left = build_cartesian_tree(arr[:root_index])
    root.right = build_cartesian_tree(arr[root_index + 1:])

    return root


def find_max_index(arr):
    max_index = 0
    max_value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_index = i
            max_value = arr[i]

    return max_index


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.key, end=" ")
        in_order_traversal(root.right)


# Usage:
arr = [4, 2, 6, 1, 3, 5, 7]
cartesian_tree = build_cartesian_tree(arr)

print("In-order traversal of the Cartesian Tree:")
in_order_traversal(cartesian_tree)
# Output: 1 2 3 4 5 6 7
