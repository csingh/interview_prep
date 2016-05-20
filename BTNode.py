class BTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def add_left_child(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right_child(self, node):
        self.right = node
        if node is not None:
            node.parent = self

    def __str__(self):
        return str(self.value)

    @staticmethod
    def print_tree(node, depth=0):
        if node is None:
            return
        else:
            BTNode.print_tree(node.right, depth+1)
            print("   "*depth + "[" + str(node.value) + "]")
            BTNode.print_tree(node.left, depth+1)

if __name__ == '__main__':
    tree = BTNode("S")
    tree.left = BTNode("L")
    tree.right = BTNode("R")
    tree.left.left = BTNode("LL")
    tree.left.right = BTNode("LR")
    tree.right.right = BTNode("RR")

    BTNode.print_tree(tree)
