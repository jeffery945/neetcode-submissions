class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt, counts = {}, {}
        for i in range(len(t)):
            countt[t[i]] = 1 + countt.get(t[i], 0)
        i, j = 0, 0
        have, need = 0, len(countt)
        res = [-1, 1]
        reslength = float("infinity")
        while j < len(s):
            counts[s[j]] = 1 + counts.get(s[j], 0)
            if s[j] in countt and counts[s[j]] == countt[s[j]]:
                have += 1
            while have == need:
                if j - i + 1 < reslength:
                    res = [i, j]
                    reslength = min(reslength, j - i + 1)

                counts[s[i]] -= 1
                if s[i] in countt and counts[s[i]] < countt[s[i]]:
                    have -= 1
                i += 1

            j += 1
        i, j = res
        return  s[i: j+ 1]if reslength != float("infinity") else ""




