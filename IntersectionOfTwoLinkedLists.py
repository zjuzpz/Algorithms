"""
160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# O(m + n)
# O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lenA, lenB = 1, 1
        curA, curB = headA, headB
        while curA.next:
            lenA += 1
            curA = curA.next
        while curB.next:
            lenB += 1
            curB = curB.next
        if curA != curB:
            return None
        curA, curB = headA, headB
        while lenA > lenB:
            curA = curA.next
            lenA -= 1
        while lenA < lenB:
            curB = curB.next
            lenB -= 1
        while curA:
            if curA == curB:
                return curA
            curA, curB = curA.next, curB.next

if __name__ == "__main__":
    headA = ListNode(1)
    headA.next = ListNode(2)
    headB = ListNode(3)
    headB.next = ListNode(4)
    headB.next.next = headA.next
    print(Solution().getIntersectionNode(headA, headB).val)
