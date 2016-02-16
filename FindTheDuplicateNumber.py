"""
287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
# O(nlogn)
# O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lower, upper = 1, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            smallOrEqual = mid
            for num in nums:
                if num <= mid:
                    smallOrEqual -= 1
            if smallOrEqual >= 0:
                lower = mid + 1
            else:
                upper = mid
        return lower

# O(n)
# O(1)
class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = 0, 0
        while fast == 0 or fast != slow:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
        fast = 0
        while nums[fast] != nums[slow]:
            fast = nums[fast]
            slow = nums[slow]
        return nums[fast]

if __name__ == "__main__":
    print(Solution().findDuplicate([2, 2, 2, 2, 2]))
