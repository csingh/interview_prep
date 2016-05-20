import sys
sys.path.insert(0, '../../')

from BTNode import *

INF = float('inf')

# TODO: deal with negative numbers
# TODO: can probably optimize with BST min/max properties

def path_sums(root, value, p_sum=0, path=[]):
    print("path:", path)

    if root is None: return 0
    if p_sum == value: return 1

    path = path[:]

    p_sum += root.value
    path.append(root.value)

    if p_sum > value:
        # we have gone over the value, so subtract the value in the
        # beginning of the path
        # TODO/NOTE: this does not account for negative numbers
        num = path.pop(0)
        p_sum -= num

    left = path_sums(root.left, value, p_sum, path)
    right = path_sums(root.right, value, p_sum, path)

    return left + right

if __name__ == '__main__':
    tree = BTNode(4)
    tree.left = BTNode(2)
    tree.left.left = BTNode(1)
    tree.left.right = BTNode(3)
    tree.right = BTNode(6)
    tree.right.left = BTNode(5)
    tree.right.left.left = BTNode(5)
    tree.right.left.left.left = BTNode(5)
    tree.right.right = BTNode(10)
    tree.right.right.right = BTNode(17)

    BTNode.print_tree(tree)

    print(path_sums(tree, 15))
    print(path_sums(tree, 20))