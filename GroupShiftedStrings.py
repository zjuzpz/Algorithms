"""
249. Group Shifted Strings
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""
# O(n ^ 2)
# O(nlogn)
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if not strings:
            return []
        s, res = sorted(strings), []
        for string in s:
            for r in res:
                if self.compare(r[0], string):
                    r.append(string)
                    break
            else:
                res.append([string])
        return res
        
    def compare(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1) == len(s2) == 0:
            return True
        count = ord(s2[0]) - ord(s1[0])
        for i in range(1, len(s1)):
            diff = ord(s2[i]) - ord(s1[i])
            if diff < 0:
                diff += 26
            if diff != count:
                return False
        return True

# O(nlogn)
# O(nlogn)
class Solution2(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if not strings:
            return []
        lookup = {}
        for string in strings:
            code = "0"
            for i in range(1, len(string)):
                diff = ord(string[i]) - ord(string[i - 1])
                if diff < 0:
                    diff += 26
                code += str(diff)
            if code in lookup:
                lookup[code].append(string)
            else:
                lookup[code] = [string]
        res = []
        for key in lookup:
            res.append(sorted(lookup[key]))
        return res

if __name__ == "__main__":
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(Solution().groupStrings(strings))
