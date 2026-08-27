class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltor, rtol = [1], [1]
        res = []
        for i in range(len(nums)):
            ltor.append(ltor[i] * nums[i])
        for i in range(len(nums) - 1, -1, -1):
            rtol.append(rtol[len(nums) - 1 -i] * nums[i])
        for i in range(len(nums)):
            res.append(ltor[i] * rtol[len(nums) - 1 - i])

        return res