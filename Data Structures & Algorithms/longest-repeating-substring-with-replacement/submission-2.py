class Solution:
    def characterReplacement(self, s: str, k: int) -> int:# sliding window
        dic = defaultdict(int)
        l = 0
        longest = 0
        mostfreq = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            mostfreq = max(mostfreq, dic[s[r]])
            if r - l + 1 - mostfreq > k:
                dic[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest