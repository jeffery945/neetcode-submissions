class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True # means if you can reach 0, means you can use nums to get i
        # dp[i] means I can get total of i right now
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                # means that if dp[i - num] can get i, dp[i] can get i
        return dp[target]