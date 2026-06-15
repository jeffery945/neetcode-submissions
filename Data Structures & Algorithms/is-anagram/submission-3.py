class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = defaultdict(int)
        dic_t = defaultdict(int)

        for word in s:
            if word in dic_s:
                dic_s[word] += 1
            else:
                dic_s[word] = 1
        for word in t:
            if word in dic_t:
                dic_t[word] += 1
            else:
                dic_t[word] = 1

        return dic_s == dic_t

