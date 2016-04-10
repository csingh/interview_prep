# http://www.practice.geeksforgeeks.org/problem-page.php?pid=297

def remove_things(string):
    string = list(string)
    num_spaces = 0
    for i in range(len(string)):
        if string[i] == "b":
            num_spaces += 1
            string[i] = ""
        elif i > 0 and string[i-1] == "a" and string[i] == "c":
            num_spaces += 2
            string[i-1] = ""
            string[i] = ""
        elif string[i] == "a" and i+1 < len(string) and string[i+1] == "c":
            pass
        elif num_spaces > 0:
            string[i-num_spaces] = string[i]
            string[i] = ""
    
    return "".join(string)

num_strings = int(raw_input())

for i in range(num_strings):
    string = str(raw_input())
    removed = remove_things(string)
    print(removed)
