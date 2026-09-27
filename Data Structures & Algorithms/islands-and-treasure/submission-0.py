class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addcell(r, c):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] == -1:
                return

            q.append([r, c])
            visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        dist = 0
        while q:
            # q stores the same dist from treasure
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addcell(r + 1, c)
                addcell(r, c + 1)
                addcell(r - 1, c)
                addcell(r, c - 1)
            dist += 1


