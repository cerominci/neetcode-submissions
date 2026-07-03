class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        row_low = 0
        row_high = rows - 1
        
        target_row = -1

        while row_low <= row_high:
            mid_row = (row_low + row_high) // 2

            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                target_row = mid_row
                break 

            elif target < matrix[mid_row][0]:
                row_high = mid_row - 1
            
            else: 
                row_low = mid_row + 1
        
        if target_row == -1:
            return False

        col_low = 0
        col_high = cols - 1
        
        while col_low <= col_high:
            mid_col = (col_low + col_high) // 2
            
            if matrix[target_row][mid_col] == target:
                return True
            elif matrix[target_row][mid_col] < target:
                col_low = mid_col + 1
            else: 
                col_high = mid_col - 1
        
        return False