"""
148. Sort List
Sort a linked list in O(n log n) time using constant space complexity.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, repr(self.next))

# O(nlogn)
# O(1)
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev, fast, slow = dummy, head, head
        while fast and fast.next:
            prev, slow, fast = prev.next, slow.next, fast.next.next
        if slow == head:
            return slow
        elif slow.next is None:
            if head.val > slow.val:
                slow.next = head
                head.next = None
                return slow
            return head
        else:
            prev.next = None
            return self.merge(self.sortList(head), self.sortList(slow))
            
    def merge(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

if __name__ == "__main__":
    head = ListNode(5)
    head.next = ListNode(9)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(6)
    print(Solution().sortList(head))
