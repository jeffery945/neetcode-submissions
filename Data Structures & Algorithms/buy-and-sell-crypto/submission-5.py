class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                revenue = prices[r] - prices[l]
                res = max(res, revenue)
            r += 1
        return res

        