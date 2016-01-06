"""
291. Word Pattern II
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.
"""
# The question is like NQueen, which can be solved by backtracking with lower time consumption!
# O(n!)
# O(n)
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.recur(pattern, str, 0, 0, {}, {})
        
    def recur(self, pattern, str, s_start, p_start, map_ps, map_sp):
        if s_start == len(str) and p_start == len(pattern):
            return True
        if s_start == len(str) or p_start == len(pattern):
            return False
        p = pattern[p_start]
        for i in range(s_start, len(str)):
            s = str[s_start: i + 1] 
            if p not in map_ps:
                if s not in map_sp or map_sp[s] == p:
                    map_ps[p], map_sp[s] = s, p
                    if self.recur(pattern, str, i + 1, p_start + 1, map_ps, map_sp):
                        return True
                    map_ps.pop(p)
                    map_sp.pop(s)
            elif map_ps[p] == s:
                if self.recur(pattern, str, i + 1, p_start + 1, map_ps, map_sp):
                    return True
        return False

if __name__ == "__main__":
    pattern = "abab"
    str = "redblueredblue"
    print(Solution().wordPatternMatch(pattern, str))
