"""
334. Increasing Triplet Subsequence
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""
# O(n)
# O(1)
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fir, sec = float("inf"), float("inf")
        for num in nums:
            if num > sec:
                return True
            if num <= fir:
                fir = num
            else:
                sec = num
        return False

if __name__ == "__main__":
    print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
