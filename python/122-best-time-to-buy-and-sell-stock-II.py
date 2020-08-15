# First past solution: 44.97%, 52ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        prev = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prev:
                profit += prices[i] - prev
            prev = prices[i]
        return profit
