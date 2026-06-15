import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # using dp
        dp = []
        dp.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                left = bisect.bisect_left(dp, nums[i])
                dp[left] = nums[i]

        return len(dp)