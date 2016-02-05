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
        flag = "-" if numerator * denominator < 0 else ""
        n, d = abs(numerator), abs(denominator)
        integer, reminder = n // d, n % d
        res = [str(integer)]
        if reminder:
            res.append(".")
        visited, index = {}, 2
        while reminder:
            n = reminder * 10
            integer, reminder = n // d, n % d
            if (integer, reminder) in visited:
                pos = visited[(integer, reminder)]
                res.insert(pos, "(")
                res.append(")")
                break
            res.append(str(integer))
            visited[(integer, reminder)] = index
            index += 1
        return flag + "".join(res)

if __name__ == "__main__":
    print(Solution().fractionToDecimal(1, 13))
