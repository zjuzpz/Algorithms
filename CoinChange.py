"""
322. Coin Change
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""
# Slower DP way
# O(n * k)
# O(n)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount < 0:
            return -1
        if amount == 0:
            return 0
        INF = 0x7ffffffe
        #Different time for INF = float("inf"), INF = 2 ** 31 - 1
        #Slowest/TLE: res = [float("inf") for i in range(amount + 1)]
        res = [INF for i in range(amount + 1)]
        coins.sort()
        for coin in coins:
            if coin < len(res):
                res[coin] = 1
        for i in range(coins[0] + 1, len(res)):
            for coin in coins:
                if coin < i:
                    res[i] = min(res[i], res[i - coin] + 1)
                else:
                    break
        return -1 if res[-1] == INF else res[-1]

# Faster BFS way
# O(n * k)
# O(k)
class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        visited, cur, count = set(coins), set(coins), 1
        while cur:
            next_turn = set()
            for num in cur:
                if num == amount:
                    return count
                for c in coins:
                    candidate = num + c
                    if candidate <= amount and candidate not in visited:
                        visited.add(candidate)
                        next_turn.add(candidate)
            cur, count = next_turn, count + 1
        return -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    print(Solution().coinChange(coins, 11))
