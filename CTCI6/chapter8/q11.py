# TODO: add back memoization?
#       -originally removed because the memo key was only using
#        n which is wrong. Need to use n and coins

def numWays(n, coins):
    # can't represent a negative number
    if n < 0: return 0

    # if we reached n == 0 then we found a combination that works
    # or if coins is empty, then we can just represent n with only pennies
    if n == 0 or not coins: return 1
    
    ways = 0
    coin = coins.pop(0) # get a coin
    numCoins = 0
    
    # recurse with using the coin in all the different ways possible:
    #       e.g. for n = 75 and coins = [25,10,5]
    #            we will take coin = 25c, and we can use it either
    #            once, twice, or three times. Then recurse with the
    #            remaining types of coins [10,5]
    while (coin*numCoins <= n):
        ways += numWays(n - coin*numCoins, coins[:])
        numCoins += 1

    return ways

def test(n, expected):
    ans = numWays(n, coins=[25,10,5])
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