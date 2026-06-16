class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hash_map = set(nums)
        for num in nums:
            if num - 1 not in hash_map:
                length = 0
                while num + length in hash_map:
                    length += 1
                longest = max(longest, length)
        return longest