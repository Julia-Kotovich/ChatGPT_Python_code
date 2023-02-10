class BTreeNode:
    def __init__(self, t, is_leaf=False):
        self.keys = []
        self.c = []
        self.t = t
        self.is_leaf = is_leaf

    def traverse(self):
        """Traverse the keys in the B-Tree."""
        for i in range(len(self.keys)):
            if not self.is_leaf:
                self.c[i].traverse()
            print(self.keys[i], end=' ')
        if not self.is_leaf:
            self.c[len(self.keys)].traverse()

    def search(self, k):
        """Search for a key in the B-Tree."""
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and k == self.keys[i]:
            return (self, i)
        elif self.is_leaf:
            return None
        else:
            return self.c[i].search(k)

    def split_child(self, i, y):
        """Split a child node of this node."""
        z = BTreeNode(y.t, y.is_leaf)
        z.keys = y.keys[y.t:]
        z.c = y.c[y.t:]
        y.keys = y.keys[:y.t-1]
        y.c = y.c[:y.t]
        self.c.insert(i+1, z)
        self.keys.insert(i, y.keys[y.t-1])
        y.c[y.t-1] = None
        y.keys[y.t-1] = None

class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t

    def traverse(self):
        """Traverse the keys in the B-Tree."""
        if self.root is not None:
            self.root.traverse()

    def search(self, k):
        """Search for a key in the B-Tree."""
        if self.root is None:
            return None
        else:
            return self.root.search(k)

    def insert(self, k):
        """Insert a key into the B-Tree."""
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(k)
        else:
            if self.root.is_full():
                s = BTreeNode(self.t, False)
                s.c.append(self.root)
                s.split_child(0
