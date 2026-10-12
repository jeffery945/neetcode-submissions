class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # the result has two options: 1. from head to the last negative number 2. from end to the first negative number. Because all we need to do is avoiding the first or the last negative number
        prefix, postfix = 0, 0
        res = nums[0]

        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            postfix = nums[len(nums) - 1 - i] * (postfix or 1)
            res = max(res, max(prefix, postfix))

        return res