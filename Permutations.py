"""
46. Permutation
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        visited = {i:False for i in range(len(nums))}
        self.recur([], visited, nums, res)
        return res
        
    def recur(self, cur, visited, nums, res):
        if len(cur) == len(nums):
            res.append(cur[:])
            return
        for i in range(len(nums)):
            if not visited[i]:
                cur.append(nums[i])
                visited[i] = True
                self.recur(cur, visited, nums, res)
                visited[i] = False
                cur.pop()

if __name__ == "__main__":
    print(Solution().permute([1,2,3]))

