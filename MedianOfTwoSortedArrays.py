"""
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""
# O(log(min(m, n)))
# O(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n =len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return self.getKth(nums1, nums2, (m + n) // 2 + 1)
        return (self.getKth(nums1, nums2, (m + n) // 2) + self.getKth(nums1, nums2, (m + n) // 2 + 1)) * 0.5
        
    def getKth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.getKth(nums2, nums1, k)
        lower, upper = 0, m - 1
        while lower <= upper:
            mid = (lower + upper) // 2
            j = k - 1 - mid
            if j < 0 or (0 <= j < n and nums1[mid] > nums2[j]):
                upper = mid - 1
            elif j >= n or (0 <= j < n and nums1[mid] < nums2[j]):
                lower = mid + 1
            else:
                return nums1[mid]
        res1, res2 = -float("inf"), -float("inf")
        if lower - 1 >= 0:
            res1 = nums1[lower - 1]
        if 0 <= k - 1 - lower < n:
            res2 = nums2[k - 1 - lower]
        return max(res1, res2)

if __name__ == "__main__":
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6, 8, 10]
    print(Solution().findMedianSortedArrays(nums1, nums2))
