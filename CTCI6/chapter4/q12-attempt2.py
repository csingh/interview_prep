# Attempt #2: after reading some hints

import sys
sys.path.insert(0, '../../')

from BTNode import *

INF = float('inf')

def get_root_to_leaf_paths(root):

    paths = []

    def paths_util(root, path=[]):
        if root.left is None and root.right is None:
            paths.append(path + [root.value])
            return
        if root.left:
            paths_util(root.left, path + [root.value])
        if root.right:
            paths_util(root.right, path + [root.value])

    paths_util(root)

    return paths

def path_sums(root, target_sum):
    num_paths = 0

    # get all paths that go from root to leaf
    paths = get_root_to_leaf_paths(root)

    for path in paths:
        # for each path, calculate running sums at each index
        running_sums = []
        p_sum = 0
        for num in path:
            p_sum += num
            running_sums.append(p_sum)

        print("path:", path, "running_sums:", running_sums)

        # now go through running sums and count how many
        # sub-paths equal to target_sum
        for i,r_sum in enumerate(running_sums):
            # if r_sum(0->i) is target_sum
            if r_sum == target_sum:
                num_paths += 1
            # if r_sum(i+1->j) is target_sum
            # but if target_sum = 0 we don't wanna subtract
            # the last item from itself, so make sure we're
            # not on the last item for this
            if (i < len(running_sums)-1) and (running_sums[-1] - r_sum == target_sum):
                num_paths += 1

    return num_paths

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