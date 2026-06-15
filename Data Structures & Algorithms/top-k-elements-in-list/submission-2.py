class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        res = []
        for num in nums:
            hash_map[num] += 1
        for i in range(k):
            res.append(max(hash_map, key=hash_map.get))
            hash_map[max(hash_map, key=hash_map.get)] = 0
        return res