class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        fresh = 0
        minute = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                pr, pc = q.popleft()
                for dr, dc in direction:
                    fr, fc = pr + dr, pc + dc
                    if fr in range(ROWS) and fc in range(COLS) and (fr, fc) not in visited and grid[fr][fc] == 1:
                        q.append((fr, fc))
                        visited.add((fr, fc))
                        fresh -= 1
            minute += 1
        
        return minute if not fresh else -1
        

        