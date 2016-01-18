"""
123. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
# O(n)
# O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        i, j, lowest, highest = 1, len(prices) - 2, prices[0], prices[-1]
        left, right = [0 for _ in prices], [0 for _ in prices]
        while i < len(prices):
            if prices[i] <= lowest:
                lowest = prices[i]
            left[i] = max(left[i - 1], prices[i] - lowest)
            if prices[j] >= highest:
                highest = prices[j]
            right[j] = max(right[j + 1], highest - prices[j])
            i, j = i + 1, j - 1
        total = [left[i] + right[i] for i in range(len(left))]
        return max(total)

class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        return self.buyKTimes(prices, 2)
        
    def buyKTimes(self, prices, k):
        buy, sell = [-float("inf") for i in prices], [0 for i in prices]
        buy[0] = -prices[0]
        for t in range(k):
            for i in range(1, len(prices)):
                buy[i] = max(buy[i], sell[i] - prices[i], buy[i - 1])
                sell[i] = max(sell[i], buy[i] + prices[i], sell[i - 1])
        return sell[-1]

if __name__ == "__main__":
    print(Solution().maxProfit([1, 2]))
