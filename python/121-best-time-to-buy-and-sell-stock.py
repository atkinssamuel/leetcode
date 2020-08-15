# First pass O(N) solution: 48ms 76.59%
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        # simple o(n^2) solution exists by computing the difference at every possible interval

        # this solution is O(N) by keeping track of the smallest left-most value:
        current_index = 1
        left = 0

        if len(prices) <= 1:
            return 0

        while current_index != len(prices):
            if prices[current_index] < prices[left]:
                left = current_index
            else:
                max_profit = max(max_profit, prices[current_index] - prices[left])
            current_index += 1

        return max_profit