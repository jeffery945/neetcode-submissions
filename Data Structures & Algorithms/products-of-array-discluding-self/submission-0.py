class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        output = [1] * len(nums)
        for i in range(len(nums) - 1):
            output[i + 1] = nums[i] * pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]
        return output 