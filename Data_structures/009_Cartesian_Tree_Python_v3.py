class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def build_cartesian_tree(arr):
    stack = []
    root = None

    for i in range(len(arr)):
        node = Node(arr[i])

        while stack and stack[-1].key > arr[i]:
            node.left = stack.pop()

        if stack:
            stack[-1].right = node
        else:
            root = node

        stack.append(node)

    while stack:
        node = stack.pop()
        if stack:
            stack[-1].right = node

    return root


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
