"""
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val, repr(self.next))

# O(n)
# O(1)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast, fir = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            sec = slow.next
            slow.next = fir
            fir, slow = slow, sec
        if fast:
            slow = slow.next
        while slow:
            if slow.val != fir.val:
                return False
            fir, slow = fir.next, slow.next
        return True

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    print(Solution().isPalindrome(head))
