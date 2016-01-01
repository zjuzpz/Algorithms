"""
320. Generalized Abbreviation
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""
# O(n * 2 ^ n)
# O(n)
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.generate(res, [], 0, word)
        return res
        
    def generate(self, res, cur, start, word):
        if start == len(word):
            res.append("".join(cur))
        else:
            cur.append(word[start])
            self.generate(res, cur, start + 1, word)
            cur.pop()
            if cur and cur[-1].isdigit():
                tem = cur[-1]
                cur[-1] = str(int(cur[-1]) + 1)
                self.generate(res, cur, start + 1, word)
                cur[-1] = tem
            else:
                cur.append("1")
                self.generate(res, cur, start + 1, word)
                cur.pop()

if __name__ == "__main__":
    print(Solution().generateAbbreviations("word"))
