"""
228. Summary Ranges
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
# O(n)
# O(1)
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res, left, right = [], nums[0], None
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                right = nums[i]
            else:
                if not right:
                    res.append(str(left))
                else:
                    res.append(str(left) + "->" + str(right))
                left, right = nums[i], None
        if not right:
            res.append(str(left))
        else:
            res.append(str(left) + "->" + str(right))
        return res

if __name__ == "__main__":
    print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
        
