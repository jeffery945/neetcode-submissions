class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return None
        resInd = 0
        reslen = 0
        
        for i in range(len(s)):
            # odd string
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    resInd = l
                    reslen = r - l + 1
                l -= 1
                r += 1

            # even string
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    resInd = l
                    reslen = r - l + 1
                l -= 1
                r += 1
        return s[resInd: resInd + reslen]