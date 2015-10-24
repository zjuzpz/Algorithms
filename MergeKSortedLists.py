"""
23. Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""
# O(nlogk)
# O(O(k))
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
        while len(lists) > 1:
            i, j = 0, len(lists) - 1
            nextLists = []
            while i < j:
                new = self.mergeTwoLists(lists[i], lists[j])
                i, j = i + 1, j - 1
                nextLists.append(new)
                if i == j:
                    nextLists.append(lists[i])
            lists = nextLists
        if not lists:
            return None
        return lists[0]
        
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

import heapq
class Solution2:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        cur = dummy
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        while heap:
            tem = heapq.heappop(heap)
            cur.next = tem[1]
            cur = cur.next
            if tem[1].next:
                heapq.heappush(heap, (tem[1].next.val, tem[1].next))
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l2 = ListNode(-3)
    l2.next = ListNode(5)
    l3 = None
    print(Solution2().mergeKLists([l1,l2,l3]))
