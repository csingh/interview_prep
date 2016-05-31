class Stack:
    def __init__(self, init_list=[]):
        self.stack = init_list

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0: return None
        return self.stack.pop(-1)

    def peek(self):
        if len(self.stack) == 0: return None
        return self.stack[-1]

    def length(self):
        return len(self.stack)

    def as_list(self):
        return self.stack

    def get_copy(self):
        return Stack(self.stack)

    def __str__(self):
        return "Stack:{}->Top".format(self.stack)

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    s = Stack()
    print(s)
    assert s.stack == []

    s.push(1)
    assert s.stack == [1]

    s.push(2)
    assert s.stack == [1,2]

    print(s)

    assert s.peek() == 2

    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == None