"""
128. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
# O(n)
# O(n)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, lookup = 0, set()
        for num in nums:
            lookup.add(num)
        for num in nums:
            cur = 1
            if num in lookup:
                lookup.remove(num)
                left, right = num - 1, num + 1
                while left in lookup:
                    lookup.remove(left)
                    left, cur = left - 1, cur + 1
                while right in lookup:
                    lookup.remove(right)
                    right, cur = right + 1, cur + 1
            res = max(res, cur)
        return res

if __name__ == "__main__":
    print (Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
