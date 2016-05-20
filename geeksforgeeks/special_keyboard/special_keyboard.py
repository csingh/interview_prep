# http://www.practice.geeksforgeeks.org/problem-page.php?pid=511

def kb(N):

    memo = dict()

    def save_to_memo(N, num_a, buff, value):
        key = (N, num_a, buff)
        memo[key] = value
        return value

    def kb_util(N, num_a, buff):

        key = (N, num_a, buff)
        if key in memo:
            return memo[key]

        if N == 0:
            return num_a
        elif N <= 2:
            # note: N is either 1 or 2
            # if N*buff > N then paste buff N times, else press a N times
            if N * buff > N:
                # paste buff N times
                return save_to_memo(N, num_a, buff,
                    kb_util(0, num_a + N*buff, buff)
                    )
            else:
                # press a N times
                return save_to_memo(N, num_a, buff,
                    kb_util(0, num_a + N, buff)
                    )
        else:
            # max of either select+copy+paste
            # or paste
            # or press a
            return save_to_memo(N, num_a, buff, max(
                kb_util(N-3, num_a * 2, num_a),
                kb_util(N-1, num_a + buff, buff),
                kb_util(N-1, num_a + 1, buff)
                ))

    return kb_util(N, 0, 0)

if __name__ == '__main__':
    for i in range(40):
        print(i, kb(i))
