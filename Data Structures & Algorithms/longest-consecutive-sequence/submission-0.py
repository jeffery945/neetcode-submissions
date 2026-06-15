class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            if num - 1 not in numset:
                leng = 1
                while (num + leng) in numset:
                    leng += 1
                longest = max(longest, leng)

        return longest