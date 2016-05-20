import sys
sys.path.insert(0, '../../')

from BTNode import *

INF = float("inf")

def check_BST(root, min_val=-INF, max_val=INF):
    if root is None: return True

    current_check = min_val <= root.value < max_val
    left_check = check_BST(root.left, min_val, root.value)
    right_check = check_BST(root.right, root.value, max_val)

    return current_check and left_check and right_check

if __name__ == '__main__':
    tree = BTNode(1)

    BTNode.print_tree(tree)
    print("--------")
    print(str(check_BST(tree)) + "\n\n")

    tree.left = BTNode(2)

    BTNode.print_tree(tree)
    print("--------")
    print(str(check_BST(tree)) + "\n\n")

    tree = BTNode(2)
    tree.left = BTNode(1)
    tree.right = BTNode(3)

    BTNode.print_tree(tree)
    print("--------")
    print(str(check_BST(tree)) + "\n\n")

    tree.left.left = BTNode(0.9)
    tree.left.right = BTNode(1)

    BTNode.print_tree(tree)
    print("--------")
    print(str(check_BST(tree)) + "\n\n")
