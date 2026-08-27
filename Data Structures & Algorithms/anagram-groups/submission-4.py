class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for st in strs:
            index = [0] * 26
            for s in st:
                index[ord(s) - ord('a')] += 1
            if tuple(index) not in hashmap:
                hashmap[tuple(index)] = []
            hashmap[tuple(index)].append(st)

        return list(hashmap.values())
