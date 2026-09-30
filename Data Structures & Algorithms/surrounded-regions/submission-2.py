class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]


        for r in range(ROWS):
            for c in range(COLS):
                if (r in (0, ROWS - 1) or c in (0, COLS - 1)) and board[r][c] == "O":
                    board[r][c] = "S"
                    q.append([r, c])
        
        while q:
                pr, pc = q.popleft()
                for dr, dc in direct:
                    fr, fc = pr + dr, pc + dc
                    if fr in range(ROWS) and fc in range(COLS) and board[fr][fc] == "O":
                        board[fr][fc] = "S"
                        q.append([fr, fc])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"