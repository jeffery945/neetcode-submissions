class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxprofit = 0
        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                if profit > maxprofit:
                    maxprofit = profit

        return maxprofit