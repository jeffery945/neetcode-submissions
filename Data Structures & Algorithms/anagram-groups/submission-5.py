class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for s in strs:
            ind = [0] * 26
            for i in s:
                ind[ord(i) - ord('a')] += 1
            if tuple(ind) not in mapp:
                mapp[tuple(ind)] = []
            mapp[tuple(ind)].append(s)
        return list(mapp.values())
