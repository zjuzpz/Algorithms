"""
288. Unique Word Abbreviation
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""
# O(n) for init O(1) for lookup
# O(1)
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.lookup = {}
        for word in dictionary:
            candidate = self.abbr(word)
            if candidate not in self.lookup:
                self.lookup[candidate] = word
            elif self.lookup[candidate] != word:
                self.lookup[candidate] = False

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.abbr(word)
        if abbr not in self.lookup:
            return True
        return self.lookup[abbr] == word
        
    def abbr(self, word):
        if len(word) == 0:
            abbr = ""
        elif len(word) == 1:
            abbr = word[0] + word[0]
        elif len(word) == 2:
            abbr = word[0] + word[1]
        else:
            abbr = word[0] + str(len(word) - 2) + word[-1]
        return abbr

if __name__ == "__main__":
    d = ["deer", "door", "cake", "card"]
    a = ValidWordAbbr(d)
    print(a.isUnique("dear"))
    print(a.isUnique("cart"))
    print(a.isUnique("cane"))
    print(a.isUnique("make"))
