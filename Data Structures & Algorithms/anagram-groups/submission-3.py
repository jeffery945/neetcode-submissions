class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1
            if tuple(count) not in hash_map:
                hash_map[tuple(count)] = []
            hash_map[tuple(count)].append(string)

        return list(hash_map.values())
