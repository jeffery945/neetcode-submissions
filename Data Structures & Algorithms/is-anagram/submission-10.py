class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts, dictt = {}, {}
        for i in range(len(s)):
            dicts[s[i]] = 1 + dicts.get(s[i], 0)
        for i in range(len(t)):
            dictt[t[i]] = 1 + dictt.get(t[i], 0)
        return dicts == dictt