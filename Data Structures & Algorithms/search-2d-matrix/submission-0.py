class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Dimensions of the matrix
        rows, cols = len(matrix), len(matrix[0])

        # Pointers for top and bottom row
        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2
            # Look at the right most value of the matrix
            if target > matrix[row][-1]:
                top = row + 1
            # If the target value was smaller than the smallest value in the row
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False