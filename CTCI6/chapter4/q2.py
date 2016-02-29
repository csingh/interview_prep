import sys
sys.path.insert(0, '/Users/chandeep/workspace/interview_prep/')

from BSTNode import *

def makeBST(sorted_arr):
    if len(sorted_arr) == 0:
        return None

    BST = BSTNode()
    middle_index = int( len(sorted_arr) / 2 )
    BST.value = sorted_arr[middle_index]

    left = makeBST(sorted_arr[:middle_index])
    BST.add_left_child(left)
    right = makeBST(sorted_arr[middle_index+1:])
    BST.add_right_child(right)

    return BST

if __name__ == '__main__':
    root = makeBST(range(1,11))
    BSTNode.print_tree(root)