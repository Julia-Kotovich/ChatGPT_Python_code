class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def build_cartesian_tree(arr):
    n = len(arr)
    return build_cartesian_tree_util(arr, 0, n-1)

def build_cartesian_tree_util(arr, start, end):
    if start > end:
        return None
    if start == end:
        return Node(arr[start])
    min_index = start
    for i in range(start+1, end+1):
        if arr[i] < arr[min_index]:
            min_index = i
    root = Node(arr[min_index])
    root.left = build_cartesian_tree_util(arr, start, min_index-1)
    root.right = build_cartesian_tree_util(arr, min_index+1, end)
    return root

arr = [9, 5, 10, 0, 6, 11, -1, 1, 2]
root = build_cartesian_tree(arr)

