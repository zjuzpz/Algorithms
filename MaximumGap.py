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
        lookup = [[None, None] for i in nums]
        gap = (max(nums) - min(nums)) // len(nums)
        minimum = min(nums)
        for num in nums:
            index = (num - minimum) // (gap + 1)
            if lookup[index] == [None, None]:
                lookup[index] = [num, num]
            else:
                lookup[index][0] = min(lookup[index][0], num)
                lookup[index][1] = max(lookup[index][1], num)
        res, right = 0, None
        for (l, r) in lookup:
            if l is not None:
                if right is not None:
                    res = max(res, l - right)
                right = r
        return res

if __name__ == "__main__":
    print(Solution().maximumGap([1, 3, 5, 16, 18, 23]))
