"""
8. String to Integer(atoi)
Implement atoi to convert a string to an integer.
"""
# O(n)
# O(1)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res, flag, str = 0, False, str.strip()
        j, index = len(str) - 1, 0
        while j >= 0:
            if not flag and str[j] == "-":
                res, flag = -res, True
            elif not flag and str[j] == "+":
                flag = True
            elif flag or not str[j].isdigit():
                flag, res, index = False, 0, 0
            else:
                res += int(str[j]) * 10 ** index
                index += 1
            j -= 1
        if res < -2 ** 31:
            return -2 ** 31
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res
if __name__ == "__main__":
    print(Solution().myAtoi("   -223  34 aa  "))
    print(Solution().myAtoi("-21233343300000009998"))
