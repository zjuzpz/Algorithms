"""
138. Copy List with Random Pointer
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# O(n)
# O(n)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        lookup, cur = {}, head
        while cur:
            lookup[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                lookup[cur].next = lookup[cur.next]
            if cur.random:
                lookup[cur].random = lookup[cur.random]
            cur = cur.next
        return lookup[head]

# O(n)
# O(1)
class Solution2(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur = head
        while cur:
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = node.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        dummy = RandomListNode(-1)
        copy, cur = dummy, head
        while cur:
            copy.next = cur.next
            cur.next = cur.next.next
            cur, copy = cur.next, copy.next
        return dummy.next


if __name__ == "__main__":
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.next.next = RandomListNode(2)
    head.next.next.next = RandomListNode(3)
    head.random = head.next.next
    result = Solution().copyRandomList(head)
    print (result.label)
    print (result.next.label)
    print (result.next.next.label)
    print (result.random.next.label)
