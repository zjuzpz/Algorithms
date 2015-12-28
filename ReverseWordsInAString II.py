"""
186. Reverse Words in a String II
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array
"""
# O(n)
# O(1)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        s.reverse()
        i, j = 0, 0
        while i < len(s):
            if s[i] == " ":
                self.swap(s, j, i - 1)
                j = i + 1
            i += 1
        self.swap(s, j, i - 1)
            
    def swap(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

if __name__ == "__main__":
    s = ["t", "h", "e", " ", "s", "k", "y", " ", \
         "i", "s", " ","b", "l", "u", "e"]
    Solution().reverseWords(s)
    print(s)
