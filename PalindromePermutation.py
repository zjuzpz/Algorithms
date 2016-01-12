"""
266. Palindrome Permutation
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""
# O(n)
# O(1)
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {}
        for i in s:
            if i not in lookup:
                lookup[i] = 1
            else:
                lookup[i] += 1
        flag = True
        for key in lookup:
            if lookup[key] % 2 == 1:
                if flag:
                    flag = False
                else:
                    return False
        return True

if __name__ == "__main__":
    print(Solution().canPermutePalindrome("carerac"))
