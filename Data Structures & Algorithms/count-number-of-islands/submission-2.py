class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append([r, c])

            while q:
                r, c = q.popleft()
                direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in direct:
                    fr, fc = r + dr, c + dc
                    if fr in range(ROWS) and fc in range(COLS) and (fr, fc) not in visited and grid[fr][fc] == "1":
                        visited.add((fr, fc))
                        q.append([fr, fc])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1

        return res
