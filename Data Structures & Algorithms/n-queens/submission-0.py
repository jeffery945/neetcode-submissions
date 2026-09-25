class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # use set to record the history

        col = set()
        postDiag = set() # r + c are the same
        negDiag = set() # r - c are the same

        res = []
        board = [["."] * n for _ in range(n)]
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or r + c in postDiag or r - c in negDiag:
                    continue

                col.add(c)
                postDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                dfs(r + 1)

                col.remove(c)
                postDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res