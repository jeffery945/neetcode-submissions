class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)
        for s_w in s:
            s_dic[s_w] += 1
        for t_w in t:
            t_dic[t_w] += 1
        return s_dic == t_dic