from binary import Tree

if __name__ == "__main__":
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.add(6)
    print("Before inversion:")
    tree.printTree()
    tree.inverse()
    print("After inversion:")
    tree.printTree()
    
