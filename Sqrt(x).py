"""
69. Sqrt(x)
Implement int sqrt(int x).
Compute and return the square root of x.
"""
# O(logn)
# O(1)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0
        index, n = -1, 1
        while n * n <= x:
            index += 1
            if n * n == x:
                return n
            n <<= 1
        res = n >> 1
        index -= 1
        while index >= 0:
            tem = (res + 2 ** index) ** 2
            if tem == x:
                return res + 2 **index
            if tem < x:
                res += 2 ** index
            index -= 1
        return res

class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        lower, upper = 1, x // 2
        while lower < upper:
            mid = (lower + upper) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                upper = mid - 1
            else:
                lower = mid + 1
        if lower ** 2 <= x:
            return lower
        return lower - 1

if __name__ == "__main__":
    print(Solution().mySqrt(3249876123))
