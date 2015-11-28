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
        lookup = set()
        for num in nums:
            lookup.add(num)
        res = 0
        for num in nums:
            if num in lookup:
                count = 1
                left = num - 1
                right = num + 1
                lookup.remove(num)
                while left in lookup:
                    count += 1
                    lookup.remove(left)
                    left -= 1
                while right in lookup:
                    count += 1
                    lookup.remove(right)
                    right += 1
                res = max(res, count)
        return res

if __name__ == "__main__":
    print (Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
