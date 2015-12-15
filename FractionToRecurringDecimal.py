"""
166. Fraction to Recurring Decimal
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
# O(logn)
# O(1)
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = -1 if numerator * denominator < 0 else 1
        n, d = abs(numerator), abs(denominator)
        integer, reminder, visited = n // d, n % d, {}
        res = [str(integer)]
        if reminder != 0:
            res.append(".")
        index = 2
        while reminder != 0:
            n = reminder * 10
            integer, reminder = n // d, n % d
            if (integer, reminder) not in visited:
                visited[(integer, reminder)] = index
                res.append(str(integer))
            else:
                pos = visited[(integer, reminder)]
                res.insert(pos, "(")
                res.append(")")
                break
            index += 1
        if flag == -1:
            res.insert(0, "-")
        return "".join(res)

if __name__ == "__main__":
    print(Solution().fractionToDecimal(1, 13))
