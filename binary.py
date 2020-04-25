from node import Node

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            self._find(value, node.left)
        elif value > node.value and node.right is not None:
            self._find(value, node.right)

    def deleteTree(self):
        self.root = None

    """Symmetric print"""
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root, 1)
            
    def _printTree(self, node, n):
        if node is not None:
            n = n + 2
            string = "  " * n
            self._printTree(node.left, n)
            print("{} {}".format(string, node.value))
            self._printTree(node.right, n)

    """Inversion print"""
    def inverse(self):
        self._inverse(self.root)

    def _inverse(self, root):
        if root is not None:
            self._inverse(root.left)
            self._inverse(root.right)

            tmp = root.left
            root.left = root.right
            root.right = tmp
