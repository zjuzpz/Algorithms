"""
47. Permutation II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""
# O(n * n!)
# O(n)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = []
        visited = {i:False for i in range(len(nums))}
        self.recur([], visited, nums, res)
        return res
        
    def recur(self, cur, visited, nums, res):
        if len(cur) == len(nums):
            res.append(cur[:])
            return
        for i in range(len(nums)):
            if not visited[i] and not (i > 0 and nums[i] == nums[i - 1] and visited[i - 1]):
                cur.append(nums[i])
                visited[i] = True
                self.recur(cur, visited, nums, res)
                visited[i] = False
                cur.pop() 

class Solution2(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        tem = nums[:]
        while True:
            res.append(tem[:])
            tem = self.nextPerm(tem)
            if tem == nums:
                return res
            
    def nextPerm(self, nums):
        if len(nums) <= 1:
            return nums
        j = len(nums) - 1
        while j > 0:
            if nums[j] > nums[j - 1]:
                i = len(nums) - 1
                while i >= j:
                    if nums[i] > nums[j - 1]:
                        nums[i], nums[j - 1] = nums[j - 1], nums[i]
                        nums[j:] = nums[:j - 1:-1]
                        return nums
                    else:
                        i -= 1
            else:
                j -= 1
        nums.reverse()
        return nums   

if __name__ == "__main__":
    print(Solution2().permuteUnique([1,1,-1,-1,1]))
