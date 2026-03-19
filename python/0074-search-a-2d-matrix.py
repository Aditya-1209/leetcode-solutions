class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows*cols - 1
        ix = -1
        while (left <= right):
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols

            if (matrix[row][col] >= target):
                ix = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if ix == -1:
            return False
        row, col = ix // cols, ix % cols
        return matrix[row][col] == target
