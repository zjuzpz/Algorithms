"""
169. Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter, res = 0, None
        for i in range(len(nums)):
            if nums[i] != res:
                if counter > 0:
                    counter -= 1
                else:
                    counter = 1
                    res = nums[i]
            else:
                counter += 1
        return res

if __name__ == "__main__":
    print(Solution().majorityElement([1,1,2,3,4,5,1,1,1]))
