"""
147. Insertion Sort List
Sort a linked list using insertion sort.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, self.next)

# O(n^2)
# O(1)
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))
        dummy.next = head
        tail = dummy
        while head:
            if head.val >= tail.val:
                head, tail = head.next, tail.next
            else:
                cur = dummy
                while cur.next.val < head.val:
                    cur = cur.next
                cur.next, head.next, head = head, cur.next, head.next
                tail.next = head
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    print(Solution().insertionSortList(head))
