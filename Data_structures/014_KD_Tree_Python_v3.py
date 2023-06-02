import numpy as np


class Node:
    def __init__(self, point, left=None, right=None, axis=0):
        self.point = point
        self.left = left
        self.right = right
        self.axis = axis


class KDTree:
    def __init__(self, points):
        self.root = None
        if points:
            self.root = self._build(points)

    def _build(self, points, depth=0):
        if not points:
            return None

        k = len(points[0])
        axis = depth % k
        points = sorted(points, key=lambda point: point[axis])
        median = len(points) // 2

        return Node(
            points[median],
            self._build(points[:median], depth + 1),
            self._build(points[median + 1:], depth + 1),
            axis
        )

    def _distance(self, point1, point2):
        return np.linalg.norm(point1 - point2)

    def _nearest_neighbor(self, point, node, depth):
        if node is None:
            return None

        k = len(point)
        axis = depth % k

        if point[axis] < node.point[axis]:
            next_node = node.left
            opposite_node = node.right
        else:
            next_node = node.right
            opposite_node = node.left

        best = self._nearest_neighbor(point, next_node, depth + 1)
        best = self._update_best(point, best, node)

        if best is None or self._distance(point, best.point) > abs(point[axis] - node.point[axis]):
            best = self._nearest_neighbor(point, opposite_node, depth + 1)

        return best

    def _update_best(self, point, best, node):
        if best is None or self._distance(point, node.point) < self._distance(point, best.point):
            return node
        return best

    def nearest_neighbor(self, point):
        return self._nearest_neighbor(point, self.root, 0).point


# Usage:
points = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
kdtree = KDTree(points)

query_point = np.array([6, 3])
nearest_neighbor = kdtree.nearest_neighbor(query_point)
print("Nearest Neighbor:", nearest_neighbor)  # Output: [5 4]
