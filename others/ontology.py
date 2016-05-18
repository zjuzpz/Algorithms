"""
Author: Peizhe Zhang
email: uclazpz@ucla.edu

Construct topic tree
For each topic(tree node), it contains a prefix tree
Given a topic(tree node), find the number of queries match
the given prefix in all its descendants and itself. 
"""
class Trie:
    def __init__(self):
        self.leaf = {}
        self.count = 0
        
    def add(self, query):
        cur = self
        cur.count += 1
        for c in query:
            if c not in cur.leaf:
                cur.leaf[c] = Trie()
            cur = cur.leaf[c]
            cur.count += 1

    def findNumber(self, query):
        cur = self
        for c in query:
            if c not in cur.leaf:
                return 0
            cur = cur.leaf[c]
        return cur.count

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.query = Trie()

class Solution:
    def __init__(self):
        self.lookup = {}
        self.root = None
        
    def constructTree(self, s):
        names = s.split()
        stack = []
        for i in xrange(len(names)):
            if names[i] == ")":
                stack.pop()
            elif names[i] != "(":
                if not stack:
                    self.root = TreeNode(names[i])
                    self.lookup[names[i]] = self.root
                    stack.append(self.root)
                else:
                    node = TreeNode(names[i])
                    self.lookup[names[i]] = node
                    stack[-1].children.add(node)
                    if i != len(names) - 1 and names[i + 1] == "(":
                        stack.append(node)

    def addQuery(self, topic, query):
        if topic not in self.lookup:
            print("No such topic!")
            return -1
        node = self.lookup[topic]
        node.query.add(query)
    
    def findNumber(self, topic, query):
        if topic not in self.lookup:
            print("No such topic!")
            return -1
        node = self.lookup[topic]
        cur = [node]
        res = 0
        while cur:
            nextTurn = []
            for topic in cur:
                res += topic.query.findNumber(query)
                for child in topic.children:
                    nextTurn.append(child)
            cur = nextTurn
        return res

def solution():
    n = int(raw_input())
    s = raw_input()
    sol = Solution()
    sol.constructTree(s)
    m = int(raw_input())
    for i in range(m):
        data = raw_input()
        topic = []
        for i in xrange(len(data)):
            if data[i] == ":":
                query = data[i + 2:].strip()
                topic = "".join(topic)
                break
            else:
                topic.append(data[i])
        sol.addQuery(topic, query)
    root = sol.root
    k = int(raw_input())
    for i in range(k):
        data = raw_input()
        topic = []
        for i in xrange(len(data)):
            if data[i] == " ":
                query = data[i + 1:].strip()
                topic = "".join(topic)
                break
            else:
                topic.append(data[i])
        print(sol.findNumber(topic, query))

solution()








