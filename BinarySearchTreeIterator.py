"""
173. Binary Search Tree Iterator
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
# O(1)
# O(1)
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cur = root

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        while self.cur:
            if not self.cur.left:
                res = self.cur
                self.cur = self.cur.right
                return res.val
            else:
                tem = self.cur.left
                while tem.right and tem.right != self.cur:
                    tem = tem.right
                if not tem.right:
                    tem.right = self.cur
                    self.cur = self.cur.left
                else:
                    res = self.cur
                    self.cur = self.cur.right
                    tem.right = None
                    return res.val

# O(1)
# O(h)
class BSTIterator2(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cur = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur or self.stack

    def next(self):
        """
        :rtype: int
        """
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        res = self.cur
        self.cur = self.cur.right
        return res.val
    

if __name__ == "__main__":
    root = TreeNode(4)
    root.left =TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    i, v = BSTIterator2(root), []
    while i.hasNext():
        v.append(i.next())
    print(v)
