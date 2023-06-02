import numpy as np

class Node:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"Node({self.point})"

class KDTree:
    def __init__(self, data):
        self.k = data.shape[1]
        self.root = self._build_tree(data, 0)

    def _build_tree(self, data, depth):
        """Build the KD Tree recursively."""
        if len(data) == 0:
            return None
        axis = depth % self.k
        data = data[data[:, axis].argsort()]
        median = len(data) // 2
        return Node(
            data[median],
            axis,
            left=self._build_tree(data[:median], depth + 1),
            right=self._build_tree(data[median + 1:], depth + 1)
        )

    def search_knn(self, point, k):
        """Search for the k nearest neighbors of a point in the KD Tree."""
        distances = []
        def search_node(node):
            if node is None:
                return
            axis = node.axis
            d = np.abs(point[axis] - node.point[axis])
            if d < np.max(distances, default=float('inf')):
                distances.append((np.linalg.norm(point - node.point), node.point))
                distances.sort(key=lambda x: x[0])
                distances = distances[:k]
            search_node(node.left if point[axis] < node.point[axis] else node.right)
            search_node(node.right if point[axis] < node.point[axis] else node.left)
        search_node(self.root)
        return [p for d, p in distances]
