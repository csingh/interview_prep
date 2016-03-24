class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # set up the data struct
        rows = []
        for x in range(numRows): rows.append("")
        
        # process the string
        cur_row = 0
        add_or_sub = 1
        for i,letter in enumerate(s):
            rows[cur_row] += letter
            cur_row += add_or_sub
            if cur_row == numRows - 1:
                # change to sub for next iter
                add_or_sub = -1
            if cur_row == 0:
                # change to add for next iter
                add_or_sub = 1
                
        # concat the strings
        ans = ""
        for s in rows:
            ans += s
            
        return ans
        
        
def test(s, numRows, expected):
    o = Solution()
    ans = o.convert(s, numRows)
    if ans == expected:
        print("Correct")
    else:
        print("Incorrect, Ans: " + str(ans) +" | Expected: " + str(expected))        

if __name__ == '__main__':
    test("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR")
    test("ABC", 3, "ABC")
    test("ABCD", 3, "ABDC")
    test("CHANDEEP", 3, "CDHNEPAE")
    test("ABCDEFG", 4, "AGBFCED")
    test("A", 3, "A")
    test("AB", 3, "AB")
    test("AB", 1, "AB")