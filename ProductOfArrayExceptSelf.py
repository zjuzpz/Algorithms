"""
238. Product of Array Except Self
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""
# O(n)
# O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = [1], [1]
        i, length = 1, len(nums)
        while i < length:
            left.append(left[-1] * nums[i - 1])
            right.append(right[-1] * nums[length - i])
            i += 1
        right.reverse()
        res = [left[i] * right[i] for i in range(len(left))]
        return res

# O(n)
# O(1)
class Solution2(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[-1] * nums[i - 1])
        tem = 1
        for i in reversed(range(1, len(nums))):
            res[i] *= tem
            tem *= nums[i]
        res[0] *= tem
        return res

if __name__ == "__main__":
    print(Solution().productExceptSelf([3, 5, 2, 6]))
