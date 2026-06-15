class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        res = []
        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1
            if tuple(count) not in hash_table:
                hash_table[tuple(count)] = []
            hash_table[tuple(count)].append(string)
        return list(hash_table.values())