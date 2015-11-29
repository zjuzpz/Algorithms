"""
164. Maximum Gap
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""
# O(n)
# O(n)
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        max_val, min_val = max(nums), min(nums)
        lookup = [[None, None] for i in range(len(nums))]
        k = (max_val - min_val) // len(nums) + 1
        if k == 0:
            return 0
        for i in range(len(nums)):
            index = (nums[i] - min_val) // k
#cannot write as index = (nums[i] - min(nums)) // k, it will exceed time limit
            if lookup[index][0] is None:
                lookup[index][0] = nums[i]
            else:
                lookup[index][0] = min(lookup[index][0], nums[i])
            if lookup[index][1] is None:
                lookup[index][1] = nums[i]
            else:
                lookup[index][1] = max(lookup[index][1] , nums[i])
        res, left, right = 0, None, None
        for i in range(len(lookup)):
            if left is None:
                left = lookup[i][1]
            elif lookup[i][0] is not None:
                right = lookup[i][0]
                res = max(res, right - left)
                left = lookup[i][1]
        return res

if __name__ == "__main__":
    print(Solution().maximumGap([1, 3, 5, 16, 18, 23]))
