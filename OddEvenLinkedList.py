"""
328. Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
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
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_odd, dummy_even = ListNode(-1), ListNode(-1)
        cur, flag = head, True
        cur_odd, cur_even = dummy_odd, dummy_even
        while cur:
            if flag:
                cur_odd.next = cur
                cur, cur_odd = cur.next, cur_odd.next
            else:
                cur_even.next = cur
                cur, cur_even = cur.next, cur_even.next
            flag = not flag
        cur_even.next = None
        cur_odd.next = dummy_even.next
        return dummy_odd.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().oddEvenList(head))
