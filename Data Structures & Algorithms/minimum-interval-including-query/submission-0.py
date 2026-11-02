class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        res = {} # because we will sort query, but the return should be as the same as original queries
        minheap = []
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]: # means q in intervals[i]
                l, r = intervals[i]
                heapq.heappush(minheap, (r - l + 1, r))
                i += 1

            while minheap and minheap[0][1] < q: # means q is not in this minimum interval anymore
                heapq.heappop(minheap)
            res[q] = minheap[0][0] if minheap else -1

        return [res[q] for q in queries]
