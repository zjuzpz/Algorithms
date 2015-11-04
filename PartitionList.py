"""
86. Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val, repr(self.next))

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next, cur = head, head
        left, right = dummy, None
        while cur:
            if cur.val < x:
                if not right:
                    cur, left = cur.next, left.next
                else:
                    left.next, cur.next, right.next = cur, left.next, cur.next
                    cur, left = right.next, left.next
            else:
                right = cur
                cur = cur.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(2)
    head.next.next.next.next.next = ListNode(4)
    print(Solution().partition(head, 4))

