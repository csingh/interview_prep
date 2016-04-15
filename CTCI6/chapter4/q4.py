import sys
sys.path.insert(0, '../../')

from BTNode import *

def check_balanced(root):

    if root is None: return (True, 0)

    left = check_balanced(root.left)
    right = check_balanced(root.right)

    return (left[1] - right[1] < 2, 1 + max(left[1],right[1]))

if __name__ == '__main__':
    tree = BTNode("S")

    BTNode.print_tree(tree)
    print("--------")
    print(str(check_balanced(tree)) + "\n\n")

    tree.left = BTNode("L")

    BTNode.print_tree(tree)
    print("--------")
    print(str(check_balanced(tree)) + "\n\n")

    tree.left.left = BTNode("LL")
    tree.left.right = BTNode("LR")

    BTNode.print_tree(tree)
    print("--------")
    print(str(check_balanced(tree)) + "\n\n")

    tree.right = BTNode("R")
    tree.right.right = BTNode("RR")

    BTNode.print_tree(tree)
    print("--------")
    print(str(check_balanced(tree)) + "\n\n")
