"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next)) 

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur, car = dummy, 0
        while l1 and l2:
            tem = l1.val + l2.val + car
            car = tem // 10
            tem = tem % 10
            cur.next = ListNode(tem)
            cur = cur.next
            l1, l2 = l1.next, l2.next
        while l1:
            tem = l1.val + car
            car = tem // 10
            tem = tem % 10
            cur.next = ListNode(tem)
            cur, l1 = cur.next, l1.next
        while l2:
            tem = l2.val + car
            car = tem // 10
            tem = tem % 10
            cur.next = ListNode(tem)
            cur, l2 = cur.next, l2.next
        if car:
            cur.next = ListNode(1)
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l = Solution().addTwoNumbers(l1, l2)
    print(l);
    
