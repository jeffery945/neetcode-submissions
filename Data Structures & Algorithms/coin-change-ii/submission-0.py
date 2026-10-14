class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(amount + 1):
            for c in range(len(coins) -1, -1, -1):
                dp[a][c] = dp[a][c + 1]
                if a >= coins[c]: # means that we can use coins[c] to form a
                    dp[a][c] += dp[a - coins[c]][c]
        return dp[amount][0]
        
