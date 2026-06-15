class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        l, r = 0, 0
        longest = 0
        while r < len(s):
            while s[r] in res:
                res.remove(s[l])
                l += 1
            res.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        return longest