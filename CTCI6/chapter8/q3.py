def magic_index(arr):

    def magic_index_util(arr, start, end):
        if start > end: return -1
        if start == end:
            if arr[start] == start:
                return start
            else:
                return -1

        mid = start + int((end-start)/2)

        if arr[mid] == mid: return mid

        if arr[mid] > mid:
            return magic_index_util(arr, start, mid-1)

        if arr[mid] < mid:
            return magic_index_util(arr, mid+1, end)

    if len(arr) < 1: return -1

    return magic_index_util(arr, 0, len(arr)-1)

if __name__ == '__main__':

    print(magic_index([]))
    print(magic_index([0]))
    print(magic_index([5]))

    print(magic_index([0,3]))
    print(magic_index([1,2]))

    print(magic_index([-1,0,1,2,4]))
    print(magic_index([-1,0,1,3,5]))
    print(magic_index([0,1,3,4,5]))