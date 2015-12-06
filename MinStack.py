"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""
# O(1)
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            self.stack.append(0)
            self.mini = x
        elif x < self.mini:
            self.stack.append(x - self.mini)
            self.mini = x
        else:
            self.stack.append(x - self.mini)
        

    def pop(self):
        """
        :rtype: nothing
        """
        tem = self.stack.pop()
        if tem < 0:
            self.mini -= tem

    def top(self):
        """
        :rtype: int
        """
        if self.stack[-1] < 0:
            return self.mini
        return self.stack[-1] + self.mini
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini
