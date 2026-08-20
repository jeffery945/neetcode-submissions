class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finalidx = len(nums) - 1
        for idx in range(len(nums) - 1, -1, -1):
            if (finalidx - idx) <= nums[idx]:
                finalidx = idx
        return finalidx == 0
