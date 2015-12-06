"""
208. Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = {}
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for w in word:
            if w not in cur.next:
                cur.next[w] = TrieNode()
            cur = cur.next[w]
        cur.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for w in word:
            if w not in cur.next:
                return False
            cur = cur.next[w]
        return cur.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for w in prefix:
            if w not in cur.next:
                return False
            cur = cur.next[w]
        return True
