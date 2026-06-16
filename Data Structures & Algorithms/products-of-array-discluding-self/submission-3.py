class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltor = [1]
        rtol = [1]
        res = []
        for num in nums:
            ltor.append(ltor[-1] * num)
        for num in nums[::-1]:
            rtol.append(rtol[-1] * num)
        for i in range(len(ltor) - 1):
            res.append(ltor[i] * rtol[-1 - i - 1])

        return res
