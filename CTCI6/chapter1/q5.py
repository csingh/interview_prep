def insertion_diff(short, long):
    skipped_one = False
    s = 0
    l = 0
    while s < len(short) and l < len(long):
        if short[s] != long[l]:
            if skipped_one: return False
            skipped_one = True
            l += 1
        else:
            s += 1
            l += 1

    return True

def replacement_diff(A, B):
    num_diffs = 0
    for i in range(len(A)):
        if A[i] != B[i]: num_diffs += 1

    return num_diffs <= 1

def one_away(A, B):
    if len(A)+1 == len(B):
        return insertion_diff(A, B)
    elif len(B)+1 == len(A):
        return insertion_diff(B, A)
    elif len(A) == len(B):
        return replacement_diff(A, B)
    else:
        return False

def test(A, B, expected):
    ans = one_away(A, B)
    if ans != expected:
        print(" #####   ERROR:", end=" ")
    else:
        print("       CORRECT:", end=" ")
    print("one_away({}, {}) = {}, expected = {}".format(A, B, ans, expected))

if __name__ == '__main__':
    test("pale", "ple", True)
    test("pales", "pale", True)
    test("pale", "bale", True)
    test("pale", "bae", False)
    test("ppal", "pal", True)
    test("pppa", "pap", False)