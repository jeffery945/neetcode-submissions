class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        minheap = [[grid[0][0], 0, 0]] # [height, row, col]
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        visited.add((0, 0))

        while minheap:
            height, pr, pc = heapq.heappop(minheap)
            if pr == N - 1 and pc == N - 1:
                return height
            for dr, dc in direct:
                fr, fc = dr + pr, dc + pc
                if fr not in range(N) or fc not in range(N) or (fr, fc) in visited:
                    continue

                visited.add((fr, fc))
                heapq.heappush(minheap, [max(height, grid[fr][fc]), fr, fc])
            