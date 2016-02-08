"""
179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s = [str(num) for num in nums]
        key = cmp_to_key(lambda x, y : int(y + x) - int(x + y))
        s.sort(key = key)
        if s and s[0] == "0":
            return "0"
        return "".join(s)
    
if __name__ == "__main__":
    num = [3, 30, 34, 5, 9]
    print (Solution().largestNumber(num)) 
