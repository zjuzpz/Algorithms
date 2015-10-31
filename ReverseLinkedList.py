"""
206. Reverse Linked List
Reverse a singly linked list.
"""
# O(n)
# O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val, repr(self.next))

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        fir, sec = dummy, dummy.next
        thr = sec.next
        while thr:
            sec.next = fir
            fir, sec, thr = sec, thr, thr.next
        sec.next = fir
        dummy.next = sec    
        head.next = None
        return dummy.next

class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

# O(n)
# O(n)
class Solution3(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        start, end = head, head.next
        tem = self.recur(start, end)
        head.next = None
        return tem
        
    def recur(self, start, end):
        if not end:
            return start
        head = self.recur(end, end.next)
        end.next = start
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(Solution().reverseList(head))
