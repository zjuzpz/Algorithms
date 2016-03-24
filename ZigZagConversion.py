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
        if numRows <= 1:
            return s
        res = []
        for i in range(numRows):
            cur = i
            while cur < len(s):
                res.append(s[cur])
                if i == 0 or i == numRows - 1:
                    cur += 2 * (numRows - 1)
                else:
                    cur += 2 * (numRows - 1 - i)
                    if cur < len(s):
                        res.append(s[cur])
                    cur += 2 * i
        return "".join(res)

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    print(Solution().convert(s, 3))
