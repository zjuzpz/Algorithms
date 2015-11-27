"""
225. Implement Stack using Queues
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.
"""
# O(n) for pop O(1) for others
# O(n)
from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.d.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        for i in range(len(self.d) - 1):
            self.d.append(self.d.popleft())
        return self.d.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.d[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.d:
            return True
        return False

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.top())
    print(s.pop())
