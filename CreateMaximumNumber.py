"""
321. Create Maximum Number
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
"""
# O(k * (m + n + k))
# O(k)
from collections import deque
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0 for i in range(k)]
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                res = max(res, self.merge(self.getKNums(nums1, i), self.getKNums(nums2, k - i)))
        return res
        
    def merge(self, nums1, nums2):
        n1, n2 = deque(nums1), deque(nums2)
        return [max(n1, n2).popleft() for i in (nums1 + nums2)]
    
    def getKNums(self, nums, k):
        drop, stack = len(nums) - k, []
        for i in range(len(nums)):
            while drop > 0 and stack and stack[-1] < nums[i]:
                drop -= 1
                stack.pop()
            stack.append(nums[i])
        return stack[0 : k]

if __name__ == "__main__":
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    print(Solution().maxNumber(nums1, nums2, 5))
