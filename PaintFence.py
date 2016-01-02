"""
276. Paint Fence
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
"""
# O(n)
# O(1)
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        num_same, num_diff = 0, k
        for i in range(n - 1):
            num_diff, num_same = (num_same + num_diff) * (k - 1), num_diff
        return num_diff + num_same

if __name__ == "__main__":
    print(Solution().numWays(3, 3))
