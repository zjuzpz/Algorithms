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
        if len(nums) <= 1:
            return 
        j = len(nums) - 1
        while j > 0:
            if nums[j] > nums[j - 1]:
                i = len(nums) - 1
                while i >= j:
                    if nums[i] > nums[j - 1]:
                        nums[i], nums[j - 1] = nums[j - 1], nums[i]
        #order function
                        nums[j:] = nums[:j - 1:-1]
                        return
                    else:
                        i -= 1
            else:
                j -= 1
        nums.reverse()
        return
        
    def order(self, nums, j):
        if (len(nums) - j) % 2 == 1:
            times = (len(nums) - j) // 2 + 1
        else:
            times = (len(nums) - j) // 2
        i = 1
        while times > 0:
            nums[j + i - 1], nums[-i] = nums[-i], nums[j + i - 1]
            i, times = i + 1, times - 1
        return

if __name__ == "__main__":
    nums = [1,2,3]
    Solution().nextPermutation(nums)
    print(nums)
