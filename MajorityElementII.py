"""
229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
"""
# O(n)
# O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        lookup = {}
        for i in range(len(nums)):
            if len(lookup) < 2:
                if nums[i] not in lookup:
                    lookup[nums[i]] = 1
                else:
                    lookup[nums[i]] += 1
            else:
                if nums[i] in lookup:
                    lookup[nums[i]] += 1
                else:
                    for key in lookup:
                        if lookup[key] == 0:
                            lookup.pop(key)
                            lookup[nums[i]] = 1
                            break
                    else:
                        for key in lookup:
                            lookup[key] -= 1
        res = []
        for key in lookup:
            count = 0
            for num in nums:
                if num == key:
                    count += 1
            if count > len(nums) // 3:
                res.append(key)
        return res

if __name__ == "__main__":
    print(Solution().majorityElement([1, 1, 1, 2, 3, 2, 4, 6]))
