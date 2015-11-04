"""
61. Rotate List
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        k %= length
        slow, fast = head, head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast.next:
            fast, slow = fast.next, slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().rotateRight(head,3))
