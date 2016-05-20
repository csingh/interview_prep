def without(str, index):
    return str[:index] + str[index+1:]

def permutations(str):
    perms = []

    def permutations_helper(str, so_far=""):
        if len(str) == 0:
            perms.append(so_far)

        already_used = dict()
        for i,letter in enumerate(str):
            if letter in already_used:
                continue
            else:
                already_used[letter] = True
                permutations_helper( without(str,i), so_far + letter )

    permutations_helper(str)

    return perms

def test(str):
    perms = permutations(str)
    print("'{}' has {} perms: {}".format(str, len(perms), perms))

if __name__ == '__main__':
    test("")
    test("a")
    test("ab")
    test("abc")
    test("abcd")
    test("aa")
    test("aaaaa")
    test("baaa")
    test("aba")