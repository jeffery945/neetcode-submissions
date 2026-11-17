class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = set(nums)
        res = 0
        for num in nums:
            length = 0
            if num - 1 not in longest:
                while num + length in longest:
                    length += 1
                    res = max(res, length)
        return res