import sys
sys.path.insert(0, '/Users/chandeep/workspace/interview_prep/CTCI6/')

from BSTNode import *
from LLNode import *

def recurser(array, node, depth=1):
    if node is None:
        return

    if len(array) < depth:
        array.append(None)
    
    new_node = LLNode(node.value)
    new_node.next = array[depth-1]
    array[depth-1] = new_node

    recurser(array, node.left, depth+1)
    recurser(array, node.right, depth+1)

def soln(tree):
    LL_array = []
    recurser(LL_array, tree)
    return LL_array

if __name__ == '__main__':
    tree = BSTNode("S")
    tree.left = BSTNode("L")
    tree.right = BSTNode("R")
    tree.left.left = BSTNode("LL")
    tree.left.right = BSTNode("LR")
    tree.right.right = BSTNode("RR")

    BSTNode.print_tree(tree)

    print("--------")

    arr = soln(tree)

    for i,x in enumerate(arr):
        print("Depth", str(i), end=": ")
        LLNode.print_list(x)
