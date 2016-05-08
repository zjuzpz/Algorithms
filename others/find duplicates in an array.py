"""
Given an array with range [1, n] inclusive, where n is the length of the array.
Find duplicate numbers in the array in O(n) time and O(1) space. (cannot swap the numbers in the array --> without using bucket sort)
"""
def findDuplicate(nums):
    res = set()
    for num in nums:
        if nums[abs(num)] < 0:
            res.add(abs(num))
        else:
            nums[abs(num)] = -nums[abs(num)]
    return res

if __name__ == "__main__":
    nums = [1, 8, 8, 2, 3, 4, 5, 5, 3]
    print(findDuplicate(nums))
    nums = [10, 2, 2, 2, 2, 6, 6, 6, 8, 8, 8, 9]
    print(findDuplicate(nums))
