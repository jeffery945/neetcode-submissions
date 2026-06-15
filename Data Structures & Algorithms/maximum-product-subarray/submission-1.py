class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max appears when all item products but without the first or last negative number
        n = len(nums)
        prefix, suffix = 0, 0
        res = nums[0]
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))

        return res

