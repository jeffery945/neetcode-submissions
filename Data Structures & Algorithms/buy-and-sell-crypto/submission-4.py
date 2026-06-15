class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = 0
        i, j = 0, 1
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            else:
                largest = max(largest, prices[j] - prices[i])
            j += 1

        return largest