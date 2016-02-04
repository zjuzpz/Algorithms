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
        if len(nums) < 2:
            return 0
        gap = (max(nums) - min(nums)) // (len(nums) + 1)
        res = [[] for i in range(len(nums) + 1)]
        minimum = min(nums)
        for num in nums:
            index = (num - minimum) // (gap + 1)
            res[index].append(num)
        maxGap, left, right = 0, None, None
        for i in range(len(res)):
            if res[i]:
                if left is None:
                    left, right = min(res[i]), max(res[i])
                else:
                    left = min(res[i])
                    maxGap = max(maxGap, left - right)
                    right = max(res[i])
        return maxGap

if __name__ == "__main__":
    print(Solution().maximumGap([1, 3, 5, 16, 18, 23]))
