"""
170. Two Sum III - Data structure design
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""
# O(1) for add O(n) for find
# O(n)
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.lookup = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number not in self.lookup:
            self.lookup[number] = 1
        else:
            self.lookup[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.lookup:
            reminder = value - key
            if reminder in self.lookup:
                if reminder != key or (reminder == key and self.lookup[key] > 1):
                    return True
        return False

if __name__ == "__main__":
    l = TwoSum()
    l.add(1)
    l.add(3)
    l.add(5)
    print(l.find(7))
