"""
219. Contains Duplicate II
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the difference between i and j is at most k.
"""
# O(n)
# O(k)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k <= 0:
            return False
        lookup = set()
        i, index = 0, 0
        while i < len(nums):
            if k > 0:
                k -= 1
                if nums[i] in lookup:
                    return True
                lookup.add(nums[i])
            else:
                if nums[i] in lookup:
                    return True
                lookup.remove(nums[index])
                lookup.add(nums[i])
                index += 1
            i += 1
        return False

if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1,2,3,2,4,3], 3))
