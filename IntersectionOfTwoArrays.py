"""
349. Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""
# O(m + n)
# O(min(m, n))
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)
        res, lookup = [], set(nums1)
        for num in nums2:
            if num in lookup:
                res.append(num)
                lookup.remove(num)
        return res

if __name__ == "__main__":
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    print(Solution().intersection(nums1, nums2))
