"""
134. Gas Station
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

# O(n)
# O(1)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total, index, tem = 0, None, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            if tem == 0 and diff >= 0:
                index = i
            tem += diff
            if tem < 0:
                tem = 0
                index = None
        if index is not None and total >= 0:
            return index
        return -1

if __name__ == "__main__":
    print(Solution().canCompleteCircuit([1,2], [2,1]))
