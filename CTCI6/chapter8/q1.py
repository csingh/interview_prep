def takesteps(n, steps=0, sequence=[]):
    if steps > n:
        return 0
    elif steps == n:
        assert sum(sequence) == n, "Sequences: {}, n: {}".format(sequence, n)
        print(sequence)
        return 1
    else:
        a = takesteps(n, steps+1, sequence + [1])
        b = takesteps(n, steps+2, sequence + [2])
        c = takesteps(n, steps+3, sequence + [3])
        return a + b + c

def test(n):
    print("Possible sequences for {} steps:".format(n))
    num_ways = takesteps(n)
    print("Total: {} sequences.".format(num_ways))

if __name__ == '__main__':
    # test(3)
    # test(4)
    # test(10)
    test(5)