class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 0: return False
        
        while (n > 1):
            n = n / 3.0
            if (n - int(n)) != 0:
                return False
        
        return True

def test(num, expected):
    s = Solution()
    ans = s.isPowerOfThree(num)
    print("isPowerOfThree({}):".format(num))
    assert ans == expected

if __name__ == '__main__':
    test(243, True)
    test(45, False)