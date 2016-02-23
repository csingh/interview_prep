class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    @staticmethod
    def print_list(node):
        if node is None:
            print("-->None")
        else:
            print("-->[" + str(node.val), end="]")
            LLNode.print_list(node.next)

if __name__ == '__main__':
    test = LLNode("Hi")
    LLNode.print_list(test)
    test.next = LLNode("yo")
    LLNode.print_list(test)
    LLNode.print_list(None)