#Select kth smallest num in nums
from random import randint
def quickSelect(nums, k):
    lower, upper = 0, len(nums) - 1
    while lower <= upper:
        pivot = randint(lower, upper)
        new_pivot = partition(nums, pivot, lower, upper)
        if new_pivot == k - 1:
            return nums[new_pivot]
        if new_pivot < k - 1:
            lower = new_pivot + 1
        else:
            upper = new_pivot - 1

def partition(nums, pivot, lower, upper):
    val, new_pivot = nums[pivot], lower
    nums[pivot], nums[upper] = nums[upper], nums[pivot]
    for i in range(lower, upper):
        if nums[i] <= val:
            nums[i], nums[new_pivot] = nums[new_pivot], nums[i]
            new_pivot += 1
    nums[new_pivot], nums[upper] = nums[upper], nums[new_pivot]
    return new_pivot

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 5, 7, 6]
    print(quickSelect(nums, 3))

