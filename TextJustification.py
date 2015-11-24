"""
68. Text Justification
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""
# O(n)
# O(1)
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, counter = [], [], 0
        for i in range(len(words)):
            if not cur:
                cur = [words[i]]
                counter = len(words[i])
            else:
                if counter + 1 + len(words[i]) <= maxWidth:
                    counter = counter + 1 + len(words[i])
                    cur.append(words[i])

                else:
                    word = cur[0]
                    if len(cur) == 1:
                        word = word + " " * (maxWidth - len(word))
                    else:
                        space = (maxWidth - counter) // (len(cur) - 1) + 1
                        extra = (maxWidth - counter) % (len(cur) - 1)
                        for j in range(1, len(cur)):
                            if extra > 0:
                                extra -= 1
                                word = word + (space + 1) * " " + cur[j]
                            else:
                                word = word + space * " " + cur[j]
                    res.append(word)
                    cur, counter = [words[i]], len(words[i])
                    
        word = " ".join(cur)
        word = word + " " * (maxWidth - len(word))
        res.append(word)
            
        return res

if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(Solution().fullJustify(words, maxWidth))
