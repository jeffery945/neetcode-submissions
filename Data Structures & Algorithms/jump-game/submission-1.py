class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pole = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if (pole - i) <= nums[i]:
                pole = i
            
        if pole == 0:
            return True
        else:
            return False