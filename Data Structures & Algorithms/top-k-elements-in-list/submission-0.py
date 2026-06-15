class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        ans = []
        for i in nums:
            res[i] += 1
        for c in range(k):
            ans.append(max(res, key=res.get))
            res[max(res, key=res.get)] = 0
        return ans