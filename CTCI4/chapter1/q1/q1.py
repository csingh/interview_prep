# Question:
#   Implement an algorithm to determine if a string has all unique characters.
#   What if you can not use additional data structures?

# with additional data structures:
#   just use a hash table to keep track of characters

# without additional data structures:
#   make an array with number of possible chars (e.g. ASCII = 256).
#   use array to count occurence of characters.

def has_unique_chars(string):
    counts = [0] * 256

    for char in string:
        i = ord(char)
        if counts[i] > 0:
            return False
        else:
            counts[i] += 1

    return True

assert has_unique_chars("") == True
assert has_unique_chars("a") == True
assert has_unique_chars("aa") == False
assert has_unique_chars("o hai") == True
assert has_unique_chars("hello") == False

print("All tests passed.")
