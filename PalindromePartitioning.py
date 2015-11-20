"""
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""
# O(2 ^ n)
# O(n)
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[""]]
        res = []
        self.recur(res, [], s)
        return res
        
    def recur(self, res, cur, s):
        if not s:
            res.append(cur[:])
            return
        for i in range(len(s)):
            if self.isPalidrome(s[0: i + 1]):
                cur.append(s[0: i + 1])
                self.recur(res, cur, s[i + 1:])
                cur.pop()
        
    def isPalidrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True

if __name__ == "__main__":
    s = "kwtbjmsjvbrwriqwxadwnufplszhqccayvdhhvscxjaqsrmrrqng\
muvxnugdzjfxeihogzsdjtvdmkudckjoggltcuybddbjoizu"
    print(len(Solution().partition(s)))
