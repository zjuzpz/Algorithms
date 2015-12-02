"""
122. Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
"""
# O(n)
# O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if not prices:
            return profit
        buy, sell = prices[0], None
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                if sell is None:
                    buy = prices[i]
                else:
                    profit += sell - buy
                    buy = prices[i]
                    sell = None
            else:
                sell = prices[i]
        if sell is not None:
            profit += sell - buy
        return profit

class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

if __name__ == "__main__":
    print(Solution().maxProfit([4, 2, 6, 7, 1, 3, 8, 9, 10]))
