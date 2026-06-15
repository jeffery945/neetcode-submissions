class Solution:
    def rob(self, nums: List[int]) -> int: #跟robber一樣 只是頭尾想一下
        
        def circular_rob(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]
        if not nums:
                return 0
        if len(nums) == 1:
            return nums[0]
        return max(circular_rob(nums[1:]), circular_rob(nums[:-1]))