"""
25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
# O(n)
# O(1)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, repr(self.next))

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1 or not head:
            return head
        dummy = ListNode(-1)
        cur = dummy
        fast = head
        while fast:
            first = fast
            second = first.next
            count = k
            while count > 0 and fast:
                count -= 1
                fast = fast.next
            if count > 0:
                cur.next = first
            else:
                third = second.next
                second.next = first
                first.next = None
                while third and third != fast:
                    first, second = second, third
                    third = third.next
                    second.next = first
                cur.next = second
                while cur.next:
                    cur = cur.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseKGroup(head, 3))
