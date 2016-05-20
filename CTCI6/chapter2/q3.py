class Node:
    def __init__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return(str(self.value))

if __name__ == '__main__':
    a = Node()
    a.value = 9
    b = Node()
    b.value = 9
    b.next = Node()
    b.next.value = 1

    sumNode = Node()
    sumPtr = sumNode
    carry = 0
    while (a is not None and b is not None):
        sum = a.value + b.value + carry
        val = sum % 10
        carry = sum // 10
        sumPtr.value = val
        sumPtr.next = Node()
        sumPtr = sumPtr.next
        a = a.next
        b = b.next
    # dont forget the carry!
    if carry == 1:
        print("hi")
        sumPtr.value = 1
