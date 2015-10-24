"""
49. Group Anagrams
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
"""
# O(nlogm) m is the max size of groups
# O(n)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res, n = [], []
        lookup = {}
        for i in range(len(strs)):
            if strs[i] == "":
                n.append("")
            else:
                s = "".join(sorted(strs[i]))
                if s not in lookup:
                    lookup[s] = [strs[i]]
                else:
                    lookup[s].append(strs[i])
        for key in lookup:
            lookup[key].sort()
            res.append(lookup[key])
        if n:
            res.append(n)
        return res

if __name__ == "__main__":
    strs = ["ac", "", "", "ca"]
    print(Solution().groupAnagrams(strs))
