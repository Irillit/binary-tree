from node import Node

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def deleteTree(self):
        self.root = None

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

    """Find values"""
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

    """Inorder non-recursive traversal"""
    def inorder_print(self):
        stack = []
        pointer = self.root

        while pointer is not None or len(stack) > 0:
            while pointer is not None:
                stack.append(pointer)
                pointer = pointer.left
            pointer = stack.pop()
            print(pointer.value, end=' ')
            pointer = pointer.right

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

    """Inversion"""
    def inverse(self):
        self._inverse(self.root)

    def _inverse(self, root):
        if root is not None:
            self._inverse(root.left)
            self._inverse(root.right)

            tmp = root.left
            root.left = root.right
            root.right = tmp

    """Max depth"""
    def depth(self):
        self.max_depth = 0
        self._depth(self.root, 0)
        return self.max_depth
        
    def _depth(self, root, n):
        if root is not None:
            n += 1
            self.max_depth = max(n, self.max_depth)
            self._depth(root.left, n)
            self._depth(root.right, n)
