"""
300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
# O(n ^ 2)
# O(n)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = [1]
        for i in range(1, len(nums)):
            cur = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    cur = max(cur, res[j])
            res.append(cur + 1)
        return max(res)

# O(nlogn)
# O(n)
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        for num in nums:
            self.insertLIS(num, LIS)
        return len(LIS)
        
    def insertLIS(self, num, LIS):
        lower, upper = 0, len(LIS) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if LIS[mid] < num:
                lower = mid + 1
            else:
                upper = mid
        print(LIS, upper)
        if upper < lower or LIS[upper] < num:
            LIS.append(num)
        else:
            LIS[upper] = num

if __name__ == "__main__":
    print(Solution2().lengthOfLIS([10, 12, 13, 14, 11, 17, 19]))
