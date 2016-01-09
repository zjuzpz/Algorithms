"""
293. Flip Game
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list [].
"""
# O(n)
# O(1)
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(s) - 1):
            if s[i] == s[i + 1] == "+":
                res.append(s[:i] + "--" + s[i + 2:])
        return res

if __name__ == "__main__":
    print(Solution().generatePossibleNextMoves("++++"))
