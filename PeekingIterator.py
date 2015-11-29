"""
284. Peeking Iterator
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.
"""
# O(1)
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.dic = iterator
        self.top = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.top:
            return self.top
        self.top = self.dic.next()
        return self.top

    def next(self):
        """
        :rtype: int
        """
        if self.top:
            res = self.top
            self.top = None
        else:
            res = self.dic.next()
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.top or self.dic.hasNext():
            return True
        return False

    
