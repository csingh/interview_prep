def rotate90(matrix):
    half = int(len(matrix)/2)
    for layer in range(half):
        start = layer
        end = len(matrix)-layer-1
        for i in range(start,end):
            # save an element in top
            temp = matrix[start][start+i]
            # assign an element in top to element from left
            matrix[start][start+i] = matrix[end-i][start]
            # assign an element in left to element from bottom
            matrix[end-i][start] = matrix[end][end-i]
            # assign an element in bottom to element from right
            matrix[end][end-i] = matrix[start+i][end]            
            # assign an element in right to temp element saved from top
            matrix[start+i][end] = temp

    return matrix

def test(matrix, expected):
    ans = rotate90(matrix)
    if ans != expected:
        print(" #####   ERROR:", end=" ")
    else:
        print("       CORRECT:", end=" ")
    print("rotate90({}) = '{}', expected = '{}'".format(matrix, ans, expected))

if __name__ == '__main__':
    test([[]], [[]])
    test([[1]], [[1]])
    test([[1,2],[3,4]], [[3,1],[4,2]])
    test([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]])
    test([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])

