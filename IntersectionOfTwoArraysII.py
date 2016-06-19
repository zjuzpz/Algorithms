"""
350. Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
# O(n)
# O(n)
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lookup = {}
        for num in nums1:
            if num not in lookup:
                lookup[num] = 0
            lookup[num] += 1
        res = []
        for num in nums2:
            if num in lookup and lookup[num] > 0:
                res.append(num)
                lookup[num] -= 1
        return res

if __name__ == "__main__":
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    print(Solution().intersect(nums1, nums2))
