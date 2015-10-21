"""
17. Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations
that the number could represent.
"""
# O(n * 4^n)
# O(n)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        lookup = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res, cur = [], ""
        self.recur(res, cur, digits, lookup)
        return res
        
    def recur(self, res, cur, digits, lookup):
        if not digits:
            res.append(cur)
            return
        if digits[0] not in lookup:
            self.recur(res, cur, digits[1:], lookup)
            return
        for i in range(len(lookup[digits[0]])):
            cur += lookup[digits[0]][i]
            self.recur(res, cur, digits[1:], lookup)
            cur = cur[0:len(cur) - 1]

if __name__ == "__main__":
    digits = "1*3#9"
    print(Solution().letterCombinations(digits))
