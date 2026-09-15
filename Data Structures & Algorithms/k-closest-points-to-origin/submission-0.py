class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        res = []
        for p in points:
            x, y = p
            heapq.heappush(maxheap, [-(x**2 + y**2), x, y])
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        while maxheap:
            dist, x, y = heapq.heappop(maxheap)
            res.append([x, y])
        return res

