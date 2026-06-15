class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                rp, cp = q.popleft()
                direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in direction:
                    r, c = rp + dr, cp + dc
                    if (r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r, c)not in visited):
                        visited.add((r, c))
                        q.append((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    res += 1

        return res


            