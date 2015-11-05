"""
43. Multiply Strings
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""
"""
        return str(int(num1) * int(num2))
        return str(eval(num1 + "*" + num2))
"""
# O(m * n)
# O(m + n)
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if int(num1) == 0 or int(num2) == 0:
            return "0"
        m, n = len(num1), len(num2)
        res = [0 for i in range(m + n)]
        for i in range(m):
            for j in range(n):
                res[i + j + 1] += int(num1[i]) * int(num2[j])
        for i in reversed(range(1, len(res))):
            res[i - 1] += res[i] // 10
            res[i] = res[i] % 10
        res = [str(i) for i in res]
        if res[0] == "0":
            del res[0]
        return "".join(res)


if __name__ == "__main__":
    num1 = "9"
    num2 = "9"
    print(Solution().multiply(num1, num2))
    
