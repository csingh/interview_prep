import sys
sys.path.insert(0, '/Users/chandeep/workspace/interview_prep/CTCI6/')

from BSTNode import *

def makeBST(sorted_arr):
    if len(sorted_arr) == 0:
        return None

    BST = BSTNode()
    middle_index = int( len(sorted_arr) / 2 )
    BST.value = sorted_arr[middle_index]

    BST.left = makeBST(sorted_arr[:middle_index])
    BST.right = makeBST(sorted_arr[middle_index+1:])

    return BST

if __name__ == '__main__':
    root = makeBST(range(1,11))
    BSTNode.print_tree(root)