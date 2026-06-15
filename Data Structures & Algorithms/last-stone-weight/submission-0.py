class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxstones = [-n for n in stones]
        while maxstones:
            if (len(maxstones) == 1):
                return -heapq.heappop(maxstones)
            elif(len(maxstones) == 0):
                return 0
            heapq.heapify(maxstones)
            large = -heapq.heappop(maxstones)
            seclarge = -heapq.heappop(maxstones)
            if (large > seclarge):
                heapq.heappush(maxstones, seclarge - large)
        return 0    