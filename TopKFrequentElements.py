"""
347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
# O(n)
# O(n)
from random import randint
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 0
            lookup[num] += 1
        frequency = list(lookup.values())
        times = self.quickSelect(frequency, k)
        res = []
        for num in lookup:
            if lookup[num] >= times:
                res.append(num)
        return res
        
    def quickSelect(self, nums, k):
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            idx = randint(lower, upper)
            newIdx = self.partition(nums, lower, upper, idx)
            if newIdx == len(nums) - k:
                return nums[newIdx]
            if newIdx > len(nums) - k:
                upper = newIdx - 1
            else:
                lower = newIdx + 1
                
    def partition(self, nums, lower, upper, idx):
        newIdx = lower
        nums[idx], nums[upper] = nums[upper], nums[idx]
        for i in range(lower, upper):
            if nums[i] <= nums[upper]:
                nums[newIdx], nums[i] = nums[i], nums[newIdx]
                newIdx += 1
        nums[newIdx], nums[upper] = nums[upper], nums[newIdx]
        return newIdx

# O(nlogk)
# O(n)
from heapq import heappush
from heapq import heappop
class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = []
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 0
            lookup[num] += 1
        for (num, frequency) in lookup.items():
            if len(h) < k:
                heappush(h, (frequency, num))
            elif h[0][0] < frequency:
                heappop(h)
                heappush(h, (frequency, num))
        res = [h[i][1] for i in range(len(h))]
        return res

if __name__ == "__main__":
    nums = [2, 1, 3, 2, 1, 1]
    k = 2
    print(Solution().topKFrequent(nums, k))
