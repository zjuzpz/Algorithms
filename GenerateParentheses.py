"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
#Catalan number
# O(4^n / n^(3/2))
# O(n)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        res = []
        self.recur(n, "", 0, 0, res)
        return res
        
    def recur(self, n, cur, left, right, res):
        if left + right == 2 * n:
    #in this recurtion, no duplicate will be generated
            res.append(cur[:])
            return 
        if left > right:
            self.recur(n, cur + ")", left, right + 1, res)
        if left < n:
            self.recur(n, cur + "(", left + 1, right, res)

if __name__ == "__main__":
    print(len(Solution().generateParenthesis(7)))
