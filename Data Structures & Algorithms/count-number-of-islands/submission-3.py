class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        q = deque()

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q.append([r, c])
            visited.add((r, c))

            while q:
                qr, qc = q.popleft()
                for dr, dc in direct:
                    fr, fc = qr + dr, qc + dc
                    if fr in range(ROWS) and fc in range(COLS) and (fr, fc) not in visited and grid[fr][fc] == "1":
                        q.append([fr, fc])
                        visited.add((fr, fc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1

        return res
