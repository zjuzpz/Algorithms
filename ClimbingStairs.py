"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
# O(n)
# O(1)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        tem1, tem2 = 1, 2
        for i in range(n - 2):
            res = tem1 + tem2
            tem1, tem2 = tem2, res
        return res

if __name__ == "__main__":
    print(Solution().climbStairs(10))
