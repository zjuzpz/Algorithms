"""
141. Linked List Cycle
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n)
# O(1)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False

if __name__ == "__main__":
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = root.next
    print(Solution().hasCycle(root))
