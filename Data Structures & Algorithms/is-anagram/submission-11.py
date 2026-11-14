class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts, dictt = {}, {}
        for i in s:
            dicts[i] = 1 + dicts.get(i, 0)
        for j in t:
            dictt[j] = 1 + dictt.get(j, 0)
        return dicts == dictt