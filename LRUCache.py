"""
146. LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
"""
import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dict = collections.OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dict:
            self.set(key, self.dict[key])
            return self.dict[key]
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            self.dict.pop(key)
            self.dict[key] = value
        else:
            if self.cap == len(self.dict):
                self.dict.popitem(last = False)
            self.dict[key] = value

if __name__ == "__main__":
    l = LRUCache(2)
    l.set(2,1)
    l.set(2,2)
    print(l.get(2))
    l.set(1,1)
    l.set(4,1)
    print(l.get(2))
    
