class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        ROW = len(heights)
        COL = len(heights[0])
        def dfs(r, c, visit, prev):
            if ((r, c) in visit or r < 0 or c < 0 or r == ROW or c == COL or heights[r][c] < prev):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COL):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROW - 1, c, atlantic, heights[ROW - 1][c])
        
        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COL - 1, atlantic, heights[r][COL - 1])

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res