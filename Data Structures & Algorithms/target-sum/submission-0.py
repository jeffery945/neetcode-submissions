class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        # dp[i][j] = using first ith items in nums to form current sum j's way is dp[i][j]

        dp[0][0] = 1 # The number of using first 0th item in nums to form current sum 0 's way is 1 way

        for i in range(len(nums)):
            for current_sum, count in dp[i].items():
                dp[i + 1][current_sum + nums[i]] += count # means using i + 1th items to form current_sum + nums[i]'s way is count
                dp[i + 1][current_sum - nums[i]] += count # we can add nums[i] and subtract nums[i]

        return dp[len(nums)][target]