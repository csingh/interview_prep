import sys
sys.path.insert(0, '../../')

from q2 import *

def successor(node):
    if node.right is not None:
        # successor is in right subtree
        # go right and recurse left until we hit leaf
        cur = node.right
        while cur.left is not None:
            cur = cur.left
        return cur
    else:
        # recurse parents until value is > node.value
        cur = node.parent
        while (cur is not None) and (cur.value <= node.value):
            cur = cur.parent
        return cur

def test(node):
    nv = node.__str__()
    sv = successor(node).__str__()
    print("Node value: {}, Successor value: {}".format(nv, sv))

if __name__ == '__main__':
    root = makeBST(range(1,11))
    BSTNode.print_tree(root)

    test(root)
    test(root.left.left.left)
    test(root.right.right)