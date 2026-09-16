class MedianFinder:

    def __init__(self):
        # [maxheap][minheap]
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if self.maxheap and num > -self.maxheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        if len(self.maxheap) > len(self.minheap) + 1:
            # maxheap has too many values
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.minheap) > len(self.maxheap) + 1:
            # minheap has too many values
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        res = 0
        if len(self.minheap) > len(self.maxheap):
            res = self.minheap[0]
        elif len(self.maxheap) > len(self.minheap):
            res = -self.maxheap[0]
        else:
            res = (-self.maxheap[0] + self.minheap[0]) / 2

        return float(res)
        