def find(A, num, start, end):
    if (end-start) == 0:
        return start

    half = (end-start) ./ 2

    if contains(A, num, start, half):
        return find(A, num, start, half)
    else:
        return find(A, num, half+1, end)

def contains(A, num, start, end):
    if A[start] <= num and num <= A[end]:
        if
