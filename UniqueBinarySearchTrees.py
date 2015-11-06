"""
96. Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# O(n ^ 2)
# O(n)
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 1]
        while n > 1:
            n -= 1
            tem = 0
            for i in range(len(res)):
                left, right = i, len(res) - 1 - i
                tem += res[left] * res[right]
            res.append(tem)
        print(res)
        return res[-1]

class Solution2:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        return self.numTrees(n - 1) * (4 * n - 2) // (n + 1)

if __name__ == "__main__":
    print(Solution().numTrees(7))
