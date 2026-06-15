class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        if len(s) != len(t):
            return False
        for i in s:
            hash_s[i] = 1 + hash_s.get(i, 0)
        for i in t:
            hash_t[i] = 1 + hash_t.get(i, 0)
        return hash_s == hash_t