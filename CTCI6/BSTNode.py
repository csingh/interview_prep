class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def print_tree(node, depth=0):
        if node is None:
            return
        else:
            BSTNode.print_tree(node.right, depth+1)
            print("   "*depth + "[" + str(node.val) + "]")
            BSTNode.print_tree(node.left, depth+1)

if __name__ == '__main__':
    tree = BSTNode("S")
    tree.left = BSTNode("L")
    tree.right = BSTNode("R")
    tree.left.left = BSTNode("LL")
    tree.left.right = BSTNode("LR")
    tree.right.right = BSTNode("RR")

    BSTNode.print_tree(tree)