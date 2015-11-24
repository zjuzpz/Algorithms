"""
82. Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, repr(self.next))

# O(n)
# O(1)
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head.next
        while cur:
            if prev.next.val == cur.val:
                cur = cur.next
            else:
                if prev.next.next == cur:
                    prev, cur = prev.next, cur.next
                else:
                    prev.next, cur = cur, cur.next
        if prev.next.next != cur:
            prev.next = cur
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    print(Solution().deleteDuplicates(head))
