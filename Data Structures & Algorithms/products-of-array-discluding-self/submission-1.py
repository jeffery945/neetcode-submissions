class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        res = [1] * len(nums)

        for i in range(len(res)):
            res[i] = pre
            pre *= nums[i]
        for i in range(len(res) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res
        