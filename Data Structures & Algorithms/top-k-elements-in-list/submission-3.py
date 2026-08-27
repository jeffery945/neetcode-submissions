class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for i in range(k):
            res.append(max(hashmap, key=hashmap.get))
            hashmap[max(hashmap, key=hashmap.get)] = 0
        return res