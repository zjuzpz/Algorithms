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
        res, cur, total = 0, gas[0] - cost[0], gas[0] - cost[0]
        for i in range(1, len(gas)):
            if cur < 0:
                cur = gas[i] - cost[i]
                res = i
            else:
                cur += gas[i] - cost[i]
            total += gas[i] - cost[i]
        return res if total >= 0 else -1

if __name__ == "__main__":
    print(Solution().canCompleteCircuit([1,2], [2,1]))
