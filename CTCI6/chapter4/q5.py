import sys
sys.path.insert(0, '../../')

from BSTNode import *

INF = float("inf")

def check_BST(root, min_val=-INF, max_val=INF):
    if root is None: return True

    current_check = min_val <= root.value < max_val
    left_check = check_BST(root.left, min_val, root.value)
    right_check = check_BST(root.right, root.value, max_val)

    return current_check and left_check and right_check

if __name__ == '__main__':
    tree = BSTNode(1)

    BSTNode.print_tree(tree)
    print("--------")
    print(str(check_BST(tree)) + "\n\n")

    tree.left = BSTNode(2)

    BSTNode.print_tree(tree)
    print("--------")
    print(str(check_BST(tree)) + "\n\n")

    tree = BSTNode(2)
    tree.left = BSTNode(1)
    tree.right = BSTNode(3)

    BSTNode.print_tree(tree)
    print("--------")
    print(str(check_BST(tree)) + "\n\n")

    tree.left.left = BSTNode(0.9)
    tree.left.right = BSTNode(1)

    BSTNode.print_tree(tree)
    print("--------")
    print(str(check_BST(tree)) + "\n\n")
