class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    @staticmethod
    def print_list(node):
        if node is None:
            print("-->None")
        else:
            print("-->[" + str(node.value), end="]")
            LLNode.print_list(node.next)

if __name__ == '__main__':
    test = LLNode("Hi")
    LLNode.print_list(test)
    test.next = LLNode("yo")
    LLNode.print_list(test)
    LLNode.print_list(None)