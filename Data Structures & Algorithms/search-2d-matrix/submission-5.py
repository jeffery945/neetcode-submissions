class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        i, j = 0, rows * cols - 1

        while i <= j:
            mid = (i + j) // 2
            row = mid // cols
            col = mid % cols
            if target < matrix[row][col]:
                j = mid - 1
            elif target > matrix[row][col]:
                i = mid + 1
            else:
                return True
        return False