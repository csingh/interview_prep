def LCS(A, B):
    memo = {}

    def save_to_memo(A,B,result):
        memo[(A,B)] = result
        return result

    def LCS_util(A,B):
        if (A,B) in memo:
            #print("poop")
            return memo[(A,B)]
        if (B,A) in memo:
            #print("poop")
            return memo[(B,A)]

        if (not A) or (not B):
            return save_to_memo(A,B,0)
        
        if A[0] == B[0]:
            return save_to_memo(A,B, 1 + LCS_util(A[1:], B[1:]))
        
        return save_to_memo(A, B, max(
            LCS_util(A[1:], B),
            LCS_util(A, B[1:])
            ))

    return LCS_util(A, B)

num = int(raw_input())

for i in range(num):
    lengths = raw_input()
    A = raw_input()
    B = raw_input()
    ans = LCS(A,B)
    print(ans)
