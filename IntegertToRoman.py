"""
12. Integer to Roman
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
"""
# O(n)
# O(1)
import collections
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        lookup = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL",\
        50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        res, keys = "", sorted(lookup.keys())
        keys.reverse()
        for i in keys:
            while num - i >= 0:
                res += lookup[i]
                num -= i
        return res

    def intToRoman2(self, num):
        res = ""
        lookup = collections.OrderedDict([(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),\
                              (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), \
                              (5, "V"), (4, "IV"), (3, "III"), (2, "II"), (1, "I")])
        for i in lookup:
            while num - i >= 0:
                res += lookup[i]
                num -= i
        return res

if __name__ == "__main__":
    print(Solution().intToRoman(3999))
    print(Solution().intToRoman2(1900))
