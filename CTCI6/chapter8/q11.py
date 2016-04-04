def numWays(n):
    memo = dict()

    def numWaysUtil(n, coins):
        if n < 0: return 0
        if n == 0 or not coins: return 1
        
        if n in memo:
            return memo[n]

        ways = 0
        coin = coins.pop(0)
        numCoins = 0
        while (coin*numCoins <= n):
            ways += numWaysUtil(n - coin*numCoins, coins[:])
            numCoins += 1

        memo[n] = ways

        return ways

    ans = numWaysUtil(n, [25,10,5])

    return ans

def test(n, expected):
    ans = numWays(n)
    if ans == expected:
        print("    Correct :", end="");
    else:
        print("##### ERROR :", end="");
    print(" numWays({}), Ans: {}, Expected: {}".format(n, ans, expected))

if __name__ == '__main__':
    for x in range(0,5):
        test(x,1)

    for x in range(5,10):
        test(x,2)

    for x in range(10,15):
        test(x,4)

    for x in range(15,20):
        test(x,6)

    for x in range(20,25):
        test(x,9)

    test(25,13)
    print(numWays(10000))