# O(nlogn)
# O(n)
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[: mid])
    right = mergeSort(nums[mid :])
    return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    while l < len(left):
        res.append(left[l])
        l += 1
    while r < len(right):
        res.append(right[r])
        r += 1
    return res

if __name__ == "__main__":
    print(mergeSort([5, 1, 7, 3, 2, 4, 6]))
