class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        res = []
        for num in nums:
            dic[num] += 1
        for i in range(k):
            res.append(max(dic, key = dic.get))
            dic[max(dic, key = dic.get)] = 0
        return res