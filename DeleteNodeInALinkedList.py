"""
237. Delete Node in a Linked List
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should
become 1 -> 2 -> 4 after calling your function.
"""
# O(1)
# O(1)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, repr(self.next))

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    node = ListNode(3)
    node.next = ListNode(4)
    head.next.next = node
    Solution().deleteNode(node)
    print(head)
