class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        visited = set()
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # 
        minheap = [[0, 0]]
        while len(visited) < N:
            cost, node = heapq.heappop(minheap)
            if node in visited:
                continue
            
            visited.add(node)
            res += cost

            for neighborCost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minheap, [neighborCost, nei])

        return res

        