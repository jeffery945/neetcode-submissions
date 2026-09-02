class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1, hash2 = {}, {}
        i, j= 0, 0
        if len(s1) > len(s2):
            return False
        for l in range(len(s1)):
            hash1[s1[l]] = 1 + hash1.get(s1[l], 0)
        
        while j < len(s2):
            hash2[s2[j]] = 1 + hash2.get(s2[j], 0)
            
            if j - i + 1 > len(s1):
                hash2[s2[i]] -= 1
                if hash2[s2[i]] == 0:
                    del hash2[s2[i]]
                i += 1
            if j - i + 1 == len(s1) and hash1 == hash2:
                return True
            j += 1
        return False
