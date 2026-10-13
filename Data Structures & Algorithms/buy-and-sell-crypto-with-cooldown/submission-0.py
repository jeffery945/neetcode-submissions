class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key = (i, buying) val = max profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying) # this cooldown means do nothing in ith day
            if buying: # if we want buying ith day
                buy = dfs(i + 1, not buying) - prices[i] # means we buy coin today, later we will sell it
                dp[(i, buying)] = max(buy, cooldown) # choose between buy or do nothing today

            else:
                sell = dfs(i + 2, not buying) + prices[i] # means we sell today, we have to wait to i + 2th day to buy another coin
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)