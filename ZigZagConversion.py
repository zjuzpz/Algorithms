"""
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
# O(n)
# O(1)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res, n = [], numRows
        if not s or n <= 1 or len(s) <= n:
            return s
        i, row = 0, 0
        while row < n:
            i = row
            res.append(s[i])
            while i < len(s):
                if row == 0 or row == n - 1:
                    i += (n - 1) * 2
                    if i < len(s):
                        res.append(s[i])
                    continue
                i += (n - 1) * 2 - 2 * row
                if i < len(s):
                    res.append(s[i])
                i += 2 * row
                if i < len(s):
                    res.append(s[i])
            row += 1
        return "".join(res)

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    print(Solution().convert(s, 3))
