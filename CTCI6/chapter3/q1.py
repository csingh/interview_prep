class ThreeStacks:
    def __init__(self, size):
        # TODO: check that size is >= some min size
        self.array = [None]*size
        self.starts = [0, size/3, 2*size/3]
        self.nexts = [0, size/3, 2*size/3]
        self.ends = [size/3 - 1, 2*size/3 - 1, size-1]

    def __str__(self):
        s = ""
        s +=   " Array : " + str(self.array)
        s += "\nStarts : " + str(self.starts)
        s += "\n  Ends : " + str(self.ends)
        s += "\n Nexts : " + str(self.starts)
        s += "\n"

        return s

    def push(self, stack_num, val):
        if self.__has_space__(stack_num):
            self.array[self.nexts(stack_num)] = val
            self.nexts[stack_num] += 1
        else:
            # we need to move stuffs
            # if next stack has space den make it smaller
            # else if prev stack has space den make it smaller
            # else error
            pass

    def __has_space__(self, stack_num):
        return self.nexts[stack_num] < self.ends[stack_num]

if __name__ == '__main__':
    stack = ThreeStacks(12)
    print(stack)
