class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def circularrob(num):
            dp = [0] * len(num)
            dp[0] = num[0]
            if len(num) == 1:
                return num[0]
            else:
                dp[1] = max(num[0], num[1])

            for i in range(2, len(num)):
                dp[i] = max(num[i] + dp[i - 2], dp[i - 1])

            return dp[-1]
        return max(circularrob(nums[1:]), circularrob(nums[:-1]))
