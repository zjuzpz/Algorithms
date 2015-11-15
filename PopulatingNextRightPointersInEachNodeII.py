"""
117. Populating Next Right Pointers in Each Node II
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        head = root
        while head:
            parent = head
            head = None
            while parent:
                if parent.left:
                    if head is None:
                        head = child = parent.left
                    else:
                        child.next = parent.left
                        child = child.next
                if parent.right:
                    if head is None:
                        head = child = parent.right
                    else:
                        child.next = parent.right
                        child = child.next
                parent = parent.next

if __name__ == "__main__":
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.right = TreeLinkNode(7)
    Solution().connect(root)
    
