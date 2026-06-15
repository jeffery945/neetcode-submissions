class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res = res^i

        for num in nums: #因為同樣的數字XOR會變０
            res = res^num

        return res
