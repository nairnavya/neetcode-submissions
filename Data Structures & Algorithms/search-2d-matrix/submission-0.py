class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        final_col_ind = len(matrix[0])-1
        top, bottom = 0, len(matrix)-1
        row_found = False
        while (top <= bottom):
            mid_tb = (top+bottom) // 2
            if target >= matrix[mid_tb][0] and target <= matrix[mid_tb][final_col_ind]:
                row_found = True
                break
            elif target < matrix[mid_tb][0]:
                bottom = mid_tb-1
            elif target > matrix[mid_tb][0] and target > matrix[mid_tb][final_col_ind]:
                top = mid_tb+1

        if row_found==True:

            left, right = 0, final_col_ind

            while (left <= right):
                mid_lr = (right+left) // 2
                if target > matrix[mid_tb][mid_lr]:
                    left = mid_lr+1
                elif target < matrix[mid_tb][mid_lr]:
                    right = mid_lr-1
                else:
                    return True
        
        return False


        # range within mid row: matrix[mid][len(matrix[0])-1]-matrix[mid][0]