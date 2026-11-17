class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltor, rtol = [1], [1]
        for num in nums:
            ltor.append(ltor[-1] * num)
        for i in range(len(nums) - 1, -1, -1):
            rtol.append(rtol[-1] * nums[i])
        res = []
        for i in range(len(nums)):
            res.append(ltor[i] * rtol[len(nums) - 1 - i])

        return res