"""
heap sort
"""
# O(nlogn)
# O(1)
def heapSort(nums):
    #Build max heap O(n)
    for i in reversed(range(0, len(nums) // 2)):
        heapify(nums, len(nums), i)
    for i in reversed(range(1, len(nums))):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def heapify(nums, end, i):
    l, r = 2 * i + 1, 2 * (i + 1)
    largest = i
    if l < end and nums[l] > nums[largest]:
        largest = l
    if r < end and nums[r] > nums[largest]:
        largest = r
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, end, largest)

if __name__ == "__main__":
    nums = [3, 5, 4, 10, 9, 7, 12, 7, 15, 11, 2, 1, 8, 6, 14, 13]
    heapSort(nums)
    print(nums)
