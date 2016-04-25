"""
345. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
"""
# O(n)
# O(n)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        i, j = 0, len(res) - 1
        while i < j:
            while i < j and res[i] not in "aeiouAEIOU":
                i += 1
            while i < j and res[j] not in "aeiouAEIOU":
                j -= 1
            if i < j:
                res[i], res[j] = res[j], res[i]
                i, j = i + 1, j - 1
        return "".join(res)

if __name__ == "__main__":
    s = "leetcode"
    print(Solution().reverseVowels(s))
