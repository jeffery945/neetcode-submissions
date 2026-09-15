class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]

        maxheap = [-n for n in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)

            if x > y:
                heapq.heappush(maxheap, y - x)
        return -maxheap[0] if maxheap else 0