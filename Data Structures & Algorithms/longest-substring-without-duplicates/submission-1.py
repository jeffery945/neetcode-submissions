class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        left = 0
        longest = 0
        for r in range(len(s)):
            
            while s[r] in hs:
                hs.remove(s[left])
                left += 1
                
            hs.add(s[r])
            longest = max(longest, r - left + 1)

        return longest