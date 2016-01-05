"""
188. Best Time to Buy and Sell Stock IV
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
# O(n) ~ O(k * n)
# O(k)
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k > len(prices) // 2:
            return self.maxProfitInfiniteTimes(prices)
        max_buy = [-float("inf") for i in range(k + 1)]
        max_buy[0] = 0
        max_sell = [0 for i in range(k + 1)]
        for i in range(len(prices)):
            for j in range(1, min(k, i // 2 + 1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j - 1] - prices[i])
                max_sell[j] = max(max_sell[j], prices[i] + max_buy[j])
        return max_sell[-1]
            
    def maxProfitInfiniteTimes(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit

if __name__ == "__main__":
    prices = [3, 1, 8, 7, 10, 2, 11, 4, 3, 13]
    print(Solution().maxProfit(3, prices))
