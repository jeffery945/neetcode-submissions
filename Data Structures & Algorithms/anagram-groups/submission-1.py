class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_hash = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in s_hash:
                s_hash[tuple(count)] = []
            s_hash[tuple(count)].append(s)
        
        return list(s_hash.values())