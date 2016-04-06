def merge(left, right):
    merged = []

    l = 0
    r = 0
    while l < len(left) or r < len(right):
        if l == len(left):
            # done with left, finish appending right
            merged.append(right[r])
            r += 1
        elif r == len(right):
            # done right right, finish appending left
            merged.append(left[l])
            l += 1
        elif left[l] <= right[r]:
            # left val is smaller, append it
            merged.append(left[l])
            l += 1
        else:
            # right val is smaller, append it
            merged.append(right[r])
            r += 1

    return merged


def merge_sort(arr):
    if len(arr) <= 1: return arr
    if len(arr) == 2: return arr if arr[0] <= arr[1] else list(reversed(arr))

    half = int(len(arr)/2)
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)

def test_merge_sort(arr):
    ans = merge_sort(arr)
    expected = sorted(arr)
    if ans == expected:
        print("       merge_sort({}) passed! ({})".format(arr, ans))
    else:
        print("ERROR: merge_sort({}) returned {}, expected: {}".format(arr,ans,expected))


if __name__ == '__main__':
    assert(merge([], []) == [])
    assert(merge([0], [0]) == [0,0])
    assert(merge([0], [1]) == [0,1])
    assert(merge([1], [0]) == [0,1])
    assert(merge([1,2,3], [1]) == [1,1,2,3])
    assert(merge([1,3,5,7], [2,4]) == [1,2,3,4,5,7])

    test_merge_sort([])
    test_merge_sort([0])
    test_merge_sort([1,2])
    test_merge_sort([1,2,3])
    test_merge_sort([5,4,99,1])
    test_merge_sort([5,1,2,7,-100])
