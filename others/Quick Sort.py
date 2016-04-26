# O(nlogn)
# O(n)
def quickSort(nums, start, end):
    if start >= end:
        return nums
    i, j, key = start, end, nums[start]
    while i < j:
        while i < j and nums[j] >= key:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        while i < j and nums[i] <= key:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    quickSort(nums, start, i - 1)
    quickSort(nums, i + 1, end)

if __name__ == "__main__":
    nums = [2, 4, 5, 1, 0, 9, 8, 8, 2, 3, 11, -3, 5]
    quickSort(nums, 0, len(nums) - 1)
    print(nums)
