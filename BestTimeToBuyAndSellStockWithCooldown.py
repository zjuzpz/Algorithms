"""
309. Best Time to Buy and Sell Stock with Cooldown
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
# O(n)
# O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy, sell, cooldown = -prices[0], 0, 0
        max_buy = -prices[0]
        for i in range(1, len(prices)):
            tem = cooldown
            cooldown = sell
            sell = max(sell, max_buy + prices[i])
            buy = tem - prices[i]
            max_buy = max(max_buy, buy)
        return sell

if __name__ == "__main__":
    print(Solution().maxProfit([1, 2, 3, 0, 2]))
