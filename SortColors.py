"""
75. Sort Colors
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note:
You are not suppose to use the library's sort function for this problem.
"""
# O(n)
# O(1)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        one, two = None, None
        for i in range(len(nums)):
            if nums[i] == 2 and two is None:
                two = i
            elif nums[i] == 1:
                if two is None and one is None:
                    one = i
                elif two is not None:
                    if one is None:
                        one = two
                    nums[two], nums[i] = nums[i], nums[two]
                    two += 1
            elif nums[i] == 0:
                if one is not None and two is not None:
                    nums[two], nums[i] = nums[i], nums[two]
                    nums[two], nums[one] = nums[one], nums[two]
                    one, two = one + 1, two + 1
                elif one is not None:
                    nums[one], nums[i] = nums[i], nums[one]
                    one += 1
                elif two is not None:
                    nums[two], nums[i] = nums[i], nums[two]
                    two += 1

class Solution2(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_zero, first_two, i = -1, len(nums), 0
        while i < first_two:
            if nums[i] == 0:
                last_zero += 1
                nums[last_zero], nums[i] = nums[i], nums[last_zero]
                i += 1
            elif nums[i] == 2:
                first_two -= 1
                nums[first_two], nums[i] = nums[i], nums[first_two]
            else:
                i += 1

if __name__ == "__main__":
    nums = [2,2,1,0,1,2,0]
    Solution().sortColors(nums)
    print(nums)
