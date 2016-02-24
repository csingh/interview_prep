class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def add_left_child(self, node):
        self.left = node
        node.parent = self

    def add_right_child(self, node):
        self.right = node
        node.parent = self

    @staticmethod
    def print_tree(node, depth=0):
        if node is None:
            return
        else:
            BSTNode.print_tree(node.right, depth+1)
            print("   "*depth + "[" + str(node.value) + "]")
            BSTNode.print_tree(node.left, depth+1)

if __name__ == '__main__':
    tree = BSTNode("S")
    tree.left = BSTNode("L")
    tree.right = BSTNode("R")
    tree.left.left = BSTNode("LL")
    tree.left.right = BSTNode("LR")
    tree.right.right = BSTNode("RR")

    BSTNode.print_tree(tree)
