class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0
        longest = 0
        mostfreq = 0
        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            mostfreq = max(mostfreq, dic[s[r]])
            while r - l + 1 - mostfreq > k:
                dic[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest