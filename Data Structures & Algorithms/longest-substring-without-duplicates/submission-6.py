class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = set()
        res = 0
        i, j = 0, 0
        while j < len(s):
            while s[j] in longest:
                longest.remove(s[i])
                i += 1
            longest.add(s[j])
            res = max(res, j - i + 1)
            j += 1
        return res
                
