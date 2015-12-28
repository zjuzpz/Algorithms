"""
246. Strobogrammatic Number
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""
# O(n)
# O(1)
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] == num[j] and num[i] in "018":
                i, j = i + 1, j - 1
            elif (num[i] == "6" and num[j] == "9") or (num[i] == "9" and num[j] == "6"):
                i, j = i + 1, j - 1
            else:
                return False
        return True

if __name__ == "__main__":
    print(Solution().isStrobogrammatic("81869818"))
