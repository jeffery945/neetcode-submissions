class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            elif r + 1 < len(prices) and prices[r + 1] < prices[r]:
                profit += prices[r] - prices[l]
                l = r
            elif r == len(prices) - 1:
                profit += prices[r] - prices[l]
            r += 1
        return profit