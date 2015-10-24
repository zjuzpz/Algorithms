"""
38. Count and Say
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
# O(n * 2^n)
# O(2^n)
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        while n > 1:
            n -= 1
            tem, count, new = res[0], 1, ""
            for i in range(1, len(res)):
                if res[i] == res[i - 1]:
                    count += 1
                else:
                    new = new + str(count) + tem
                    tem = res[i]
                    count = 1
            res = new + str(count) + tem
        return res

if __name__ == "__main__":
    print(Solution().countAndSay(4))
