"""
278. First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

def isBadVersion(version):
    if version >= 5:
        return True
    return False

# O(logn)
# O(1)
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower, upper = 1, n
        while lower < upper:
            mid = (lower + upper) // 2
            if isBadVersion(mid):
                upper = mid
            else:
                lower = mid + 1
        return lower

if __name__ == "__main__":
    print(Solution().firstBadVersion(20))
