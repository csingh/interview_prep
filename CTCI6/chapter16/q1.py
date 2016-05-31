import sys
sys.path.insert(0, '../../PythonFunctionTest')
from FunctionTester import *

import random


def number_swapper(a,b):
    a = b - a
    b = b - a
    a = a + b

    return (a,b)

if __name__ == '__main__':
    FT = FunctionTester(number_swapper)

    FT.addTest( (0,0), 0, 0 )

    random.seed(50)
    for x in range(10):
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        FT.addTest( (b,a), a, b )

    FT.runTests()
