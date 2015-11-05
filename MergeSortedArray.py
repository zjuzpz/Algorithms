"""
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements
initialized in nums1 and nums2 are m and n respectively.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[j] = nums1[m - 1]
                m -= 1
            else:
                nums1[j] = nums2[n - 1]
                n -= 1
            j -= 1
        while m > 0:
            nums1[j] = nums1[m - 1]
            m, j = m - 1, j - 1
        while n > 0:
            nums1[j] = nums2[n - 1]
            n, j = n - 1, j - 1

if __name__ == "__main__":
    nums1 = [2,3,1,4]
    m = 2
    nums2 = [1,5]
    n = 2
    Solution().merge(nums1, m , nums2, n)
    print(nums1)
    
