from binary import Tree

if __name__ == "__main__":
    tree = Tree()
    tree.add(2)
    tree.add(1)
    tree.add(3)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.add(6)
    print("Before inversion:")
    tree.printTree()
    tree.inverse()
    print("Inorder:")
    tree.inorder_print()
    print("Max depth: ", end='')
    depth = tree.depth()
    print(depth)
    print("\nAfter inversion:")
    tree.printTree()
    print("Validation: ")
    print(tree.validate())
    
