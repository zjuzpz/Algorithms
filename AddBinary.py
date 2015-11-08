"""
67. Add Binary
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
# O(n)
# O(1)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 and j >= 0:
            carry = self.adder(res, a[i], b[j], carry)
            i, j = i - 1, j - 1
        while i >= 0:
            carry = self.adder(res, a[i], "0", carry)
            i -= 1
        while j >= 0:
            carry = self.adder(res, b[j], "0", carry)
            j -= 1
        if carry == 1:
            res.append("1")
        res.reverse()
        return "".join(res)
                
    def adder(self, res, a, b, carry):
        tem = carry + int(a) + int(b)
        if tem == 3:
            carry = 1
            res.append("1")
        elif tem == 2:
            carry = 1
            res.append("0")
        elif tem == 1:
            carry = 0
            res.append("1")
        else:
            carry = 0
            res.append("0")
        return carry

if __name__ == "__main__":
    print(Solution().addBinary("10101", "101"))
