class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashs1, hashs2 = {}, {}
        l, r = 0, 0
        for i in range(len(s1)):
            hashs1[s1[i]] = 1 + hashs1.get(s1[i], 0)
        while r < len(s2):
            hashs2[s2[r]] = 1 + hashs2.get(s2[r], 0)
            if r - l + 1 > len(s1):
                hashs2[s2[l]] -= 1
                if hashs2[s2[l]] == 0:
                    del hashs2[s2[l]]
                l += 1
            if r - l + 1 == len(s1) and hashs1 == hashs2:
                return True
            r += 1

        return False
