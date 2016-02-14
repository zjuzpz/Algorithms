"""
312. Burst Balloons
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
# O(n ^ 3)
# O(n ^ 2)
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        coins = [1] + [num for num in nums if num != 0] + [1]
        n = len(coins)
        res = [[0 for j in range(n)] for i in range(n)]
        for i in range(2, n):
            for left in range(n - i):
                right = left + i
                for j in range(left + 1, right):
                    res[left][right] = max(res[left][right], res[left][j] + res[j][right] + \
                    coins[left] * coins[j] * coins[right])
        return res[0][n - 1]

class Solution2(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = [[0 for j in range(len(nums))] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in reversed(range(0, i + 1)):
                if i == j:
                    left = nums[i - 1] if i >= 1 else 1
                    right = nums[i + 1] if i < len(nums) - 1 else 1
                    res[i][j] = nums[i] * left * right
                else:
                    for k in range(j, i + 1):
                        left = 0 if k == j else res[k - 1][j]
                        right = 0 if k == i else res[i][k + 1]
                        l = nums[j - 1] if j >= 1 else 1
                        r = nums[i + 1] if i < len(nums) - 1 else 1
                        res[i][j] = max(res[i][j], left + right + nums[k] * l * r)
        return res[-1][0]

if __name__ == "__main__":
    nums = [3, 1, 5, 8]
    print(Solution2().maxCoins(nums))
