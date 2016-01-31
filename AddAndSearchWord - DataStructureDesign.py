"""
211. Add and Search Word - Data structure design
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
# O(min(n, h))
# O(min(n, h))
class TrieNode(object):
    def __init__(self):
        self.isString = False
        self.node = {}
    
    
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if not word:
            self.root.isString = True
        cur = self.root
        for p in word:
            if p not in cur.node:
                cur.node[p] = TrieNode()
            cur = cur.node[p]
        cur.isString = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, self.root, 0)
        
    def searchHelper(self, word, cur, start):
        if start == len(word):
            return cur.isString
        if word[start] in cur.node:
            return self.searchHelper(word, cur.node[word[start]], start + 1)
        elif word[start] == ".":
            for p in cur.node:
                if self.searchHelper(word, cur.node[p], start + 1):
                    return True
        return False


"""
    def search(self, word):
        if not word:
            return self.root.isString
        lookup = [self.root]
        for c in word:
            if not lookup:
                return False
            next_turn = []
            if c == ".":
                for cur in lookup:
                    for key in cur.node:
                        next_turn.append(cur.node[key])
            else:
                for cur in lookup:
                    if c in cur.node:
                        next_turn.append(cur.node[c])
            lookup = next_turn
        for cur in lookup:
            if cur.isString:
                return True
        return False
"""
        
if __name__ == "__main__":
    d = WordDictionary()
    d.addWord("worda")
    d.addWord("wordb")
    print(d.search("worda"))
    print(d.search("wordc"))
