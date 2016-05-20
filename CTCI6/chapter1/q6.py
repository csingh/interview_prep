def string_compression(string):
    if len(string) < 3:
        # can't save anything on strings this size
        return string

    compressed = ""

    prev = string[0]
    count = 1

    for i in range(1, len(string)+1):
        if i == len(string) or prev != string[i]:
            # end of string or letter changed
            compressed += prev + str(count)
            count = 1
        else:
            count += 1

        if i < len(string):
            prev = string[i]

    return compressed if len(compressed) < len(string) else string

def test(string, expected):
    ans = string_compression(string)
    if ans != expected:
        print(" #####   ERROR:", end=" ")
    else:
        print("       CORRECT:", end=" ")
    print("string_compression({}) = '{}', expected = '{}'".format(string, ans, expected))

if __name__ == '__main__':
    test("", "")
    test("h", "h")
    test("hi", "hi")
    test("hii", "hii")
    test("hhii", "hhii")
    test("hhhii", "h3i2")
    test("fffffffuuuuuuuuuuuu", "f7u12")
    test("aabcccccaaad", "a2b1c5a3d1")
