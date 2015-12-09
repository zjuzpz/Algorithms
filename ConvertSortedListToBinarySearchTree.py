"""
109. Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(n)
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        prev, slow, fast = dummy, head, head
        while fast and fast.next:
            prev, slow, fast = prev.next, slow.next, fast.next.next
        prev.next = None
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(dummy.next)
        node.right = self.sortedListToBST(slow.next)
        return node

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    root = Solution().sortedListToBST(head)
    print(root.left.val, root.val, root.right.val)
