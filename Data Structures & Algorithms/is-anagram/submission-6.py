class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = defaultdict(int)
        c_t = defaultdict(int)
        for c in s:
            c_s[c] += 1
        for c in t:
            c_t[c] += 1

        return c_s == c_t