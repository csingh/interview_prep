import sys
sys.path.insert(0, '../../')

from BTNode import *
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
    tree = BTNode("S")
    tree.left = BTNode("L")
    tree.right = BTNode("R")
    tree.left.left = BTNode("LL")
    tree.left.right = BTNode("LR")
    tree.right.right = BTNode("RR")

    BTNode.print_tree(tree)

    print("--------")

    arr = soln(tree)

    for i,x in enumerate(arr):
        print("Depth", str(i), end=": ")
        LLNode.print_list(x)
