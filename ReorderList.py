"""
143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        dummy = ListNode(-1)
        dummy.next = head
        prev, fast, slow = dummy, head, head
        while fast and fast.next:
            fast, slow, prev = fast.next.next, slow.next, prev.next
        prev.next, first, second = None, slow, slow.next
        first.next = None
        while second:
            third = second.next
            second.next = first
            first, second = second, third
        cur_1, cur_2 = head, first
        while cur_1 and cur_1 is not cur_2:
            prev, cur_2 = cur_2, cur_2.next
            if cur_1.next:
                prev.next = cur_1.next
            cur_1.next = prev
            cur_1 = prev.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    Solution().reorderList(head)
    print(head)
