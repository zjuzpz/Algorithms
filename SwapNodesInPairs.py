"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, self.next)

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        fir, sec = dummy, dummy.next
        while fir and sec:
            thr = sec.next
            if not thr:
                return dummy.next
            fir.next = thr
            fir = thr.next
            thr.next = sec
            sec.next = fir
            sec, fir = fir, sec
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    print(Solution().swapPairs(head))
