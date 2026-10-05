class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append([v, w])

        minheap = [(0, k)] # (the weight from start to node, node#)
        res = 0
        visited = set()

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = w1

            # visit all the neighbors of the node
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap, (w1 + w2, n2))
        return res if len(visited) == n else -1