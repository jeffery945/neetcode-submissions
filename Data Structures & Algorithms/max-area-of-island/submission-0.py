class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        visited = set()
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def bfs(r, c):
            q = deque()
            q.append([r, c])
            visited.add((r, c))
            res = 1
            while q:
                r, c = q.popleft()
                for dr, dc in direct:
                    fr, fc = r + dr, c + dc
                    if fr in range(ROWS) and fc in range(COLS) and (fr, fc) not in visited and grid[fr][fc] == 1:
                        q.append([fr, fc])
                        visited.add((fr, fc))
                        res += 1
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area