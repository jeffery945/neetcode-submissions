class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c + 1] # means that I would like summation to matrix[r - 1][c]
                self.sumMatrix[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottom_right = self.sumMatrix[row2][col2]
        bottom_left = self.sumMatrix[row2][col1 - 1]
        top_right = self.sumMatrix[row1 - 1][col2]
        top_left = self.sumMatrix[row1 - 1][col1 - 1]
        return bottom_right - bottom_left - top_right + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)