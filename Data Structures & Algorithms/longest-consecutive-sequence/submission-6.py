class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in longest:
                length = 0
                while num + length in longest:
                    length += 1
                    res = max(res, length)
        return res