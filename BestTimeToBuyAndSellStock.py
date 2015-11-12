"""
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
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
        res = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - buy)
            if prices[i] < buy:
                buy = prices[i]
        return res

if __name__ == "__main__":
    print(Solution().maxProfit([2,1,4,1,2,6,1,3]))
