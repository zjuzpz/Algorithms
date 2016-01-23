"""
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
# O(n)
# O(1)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = None
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                index = i
        if index is None:
            self.swap(nums, 0, len(nums) - 1)
            return
        for i in range(index + 1, len(nums)):
            if nums[i] > nums[index]:
                a = i
            else:
                break
        nums[index], nums[a] = nums[a], nums[index]
        self.swap(nums, index + 1, len(nums) - 1)
        
    def swap(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

if __name__ == "__main__":
    nums = [1,2,3]
    Solution().nextPermutation(nums)
    print(nums)
