class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mostfreq = 0
        i, j = 0, 0
        res = 0
        lis = {}
        while j < len(s):
            lis[s[j]] = 1 + lis.get(s[j], 0)
            mostfreq = max(mostfreq, lis[s[j]])
            
            if j - i + 1 - mostfreq > k:
                lis[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1

        return res