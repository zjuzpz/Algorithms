"""
92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        left = dummy
        while m > 1:
            m -= 1
            n -= 1
            left = left.next
        cur = left.next
        while n > 1:
            sec = cur.next.next
            left.next, cur.next.next, cur.next = cur.next, left.next, sec
            n -= 1
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseBetween(head, 2, 4))
