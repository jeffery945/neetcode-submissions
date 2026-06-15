class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, countS = {}, {}
        
        #create t table
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        l = 0
        have, need = 0, len(countT)
        res = [-1, -1]
        reslength = float("infinity")
        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c, 0)
            # if satisfy the requirement, have plus one
            if c in countT and countT[c] == countS[c]:
                have += 1

            while have == need:
                if (r - l + 1) < reslength:
                    res = [l, r]
                    reslength = r - l + 1
                # pop the left and decrease the countS and have
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if reslength != float("infinity") else ""

