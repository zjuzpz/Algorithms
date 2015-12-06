"""
220. Contains Duplicate III
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t
and the difference between i and j is at most k.
"""
# O(n)
# O(k)
import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        d = collections.OrderedDict()
        for num in nums:
            if len(d) > k:
                d.popitem(False)
            bucket = num if not t else num // t
            for neighbor in (d.get(bucket - 1), d.get(bucket), d.get(bucket + 1)):
                if neighbor is not None and abs(neighbor - num) <= t:
                    return True
            d[bucket] = num
        return False

if __name__ == "__main__":
    nums = [4, 9, 0, 7, 5, 2, 8, 7]
    print(Solution().containsNearbyAlmostDuplicate(nums, 3, 2))
