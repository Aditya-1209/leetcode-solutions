class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left, right = 0, len(row) - 1
            ix = -1

            while left <= right:
                mid = (left + right) >> 1

                if row[mid] >= target:
                    ix = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            if ix != -1 and row[ix] == target:
                return True
        
        return False
