"""
23. Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""
# O(nlogk)
# O(k)
# Merge sort, heap
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.val,repr(self.next))

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return 
        while len(lists) > 1:
            i, j, next = 0, len(lists) - 1, []
            while i <= j:
                if i == j:
                    next.append(lists[i])
                else:
                    next.append(self.mergeTwoList(lists[i], lists[j]))
                i, j = i + 1, j - 1
            lists = next
        return lists[0]
        
    def mergeTwoList(self, l1, l2):
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

from heapq import heappush
from heapq import heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        for l in lists:
            if l:
                heappush(h, (l.val, l))
        dummy = ListNode(-1)
        cur = dummy
        while h:
            tem = heappop(h)
            cur.next = tem[1]
            cur = cur.next
            if tem[1].next:
                heappush(h, (tem[1].next.val, tem[1].next))
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l2 = ListNode(-3)
    l2.next = ListNode(5)
    l3 = None
    print(Solution().mergeKLists([l1,l2,l3]))
