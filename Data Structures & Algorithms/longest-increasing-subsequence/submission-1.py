from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        res.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                left = bisect_left(res, nums[i])
                res[left] = nums[i]

        return len(res)
