"""
187. Repeated DNA Sequences
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""
# O(n)
# O(n)
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        lookup, res = {}, []
        for i in range(len(s) - 9):
            seq = s[i : i + 10]
            if seq not in lookup:
                lookup[seq] = False
            elif not lookup[seq]:
                lookup[seq] = True
                res.append(seq)
        return res

if __name__ == "__main__":
    print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))
