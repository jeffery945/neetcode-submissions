class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = defaultdict(int)
        dic_t = defaultdict(int)
        for s_char in s:
            if s_char in dic_s:
                dic_s[s_char] += 1
            else:
                dic_s[s_char] = 1
        for t_char in t:
            if t_char in dic_t:
                dic_t[t_char] += 1
            else:
                dic_t[t_char] = 1
        return dic_s == dic_t