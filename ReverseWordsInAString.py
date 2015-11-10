"""
151. Reverse Words in a String
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""
# O(n)
# O(n)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words, left = [], None
        for i in range(len(s)):
            if s[i] != " " and left is None:
                left = i
            elif s[i] == " " and left is not None:
                words.append(s[left : i])
                left = None
        if left is not None:
            words.append(s[left:])
        if not words:
            return ""
        words[0] = words[0].strip()
        i, j = 0, len(words) - 1
        while i < j:
            words[i], words[j] = words[j], words[i]
            i, j = i + 1, j - 1
        return " ".join(words)

class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))

if __name__ == "__main__":
    s = "  a   b "
    print(Solution().reverseWords(s))
