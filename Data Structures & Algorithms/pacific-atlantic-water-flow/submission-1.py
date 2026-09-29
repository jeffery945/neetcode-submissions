class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic, pacific = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        q = deque()
        direct = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def bfs(r, c, visited):
            q.append([r, c])
            visited.add((r, c))
            while q:
                pr, pc = q.popleft()
                for dr, dc in direct:
                    fr, fc = dr + pr, dc + pc
                    if fr in range(ROWS) and fc in range(COLS) and (fr, fc) not in visited and heights[fr][fc] >= heights[pr][pc]:
                        q.append([fr, fc])
                        visited.add((fr, fc))

        for c in range(COLS):
            bfs(0, c, pacific)
            bfs(ROWS - 1, c, atlantic)
        for r in range(ROWS):
            bfs(r, 0, pacific)
            bfs(r, COLS - 1, atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res