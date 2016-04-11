import sys
sys.path.insert(0, '../../')

from BSTNode import *

def check_balanced(root):

    if root is None: return (True, 0)

    left = check_balanced(root.left)
    right = check_balanced(root.right)

    return (left[1] - right[1] < 2, 1 + max(left[1],right[1]))

if __name__ == '__main__':
    tree = BSTNode("S")

    BSTNode.print_tree(tree)
    print("--------")
    print(str(check_balanced(tree)) + "\n\n")

    tree.left = BSTNode("L")

    BSTNode.print_tree(tree)
    print("--------")
    print(str(check_balanced(tree)) + "\n\n")

    tree.left.left = BSTNode("LL")
    tree.left.right = BSTNode("LR")

    BSTNode.print_tree(tree)
    print("--------")
    print(str(check_balanced(tree)) + "\n\n")

    tree.right = BSTNode("R")
    tree.right.right = BSTNode("RR")

    BSTNode.print_tree(tree)
    print("--------")
    print(str(check_balanced(tree)) + "\n\n")
