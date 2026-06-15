class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        while i < j:
            mid = (i + j + 1) // 2
            if matrix[mid][0] <= target:
                i = mid
            else:
                j = mid - 1
        for ind in range(len(matrix[0])):
            if matrix[i][ind] == target:
                return True
        return False
