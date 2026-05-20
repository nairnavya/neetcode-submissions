class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
       nums = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
       for row in range(0, 9):
            for column in range(0,9):
                tilenum = board[row][column]
                if tilenum != '.':
                    nums[tilenum] += 1
            if any(y > 1 for y in nums.values()):
                return False
            for key in nums: nums[key] = 0
        
       for column in range(0, 9):
            for row in range(0,9):
                tilenum = board[row][column]
                if tilenum != '.':
                    nums[tilenum] += 1
            if any(y > 1 for y in nums.values()):
                return False
            for key in nums: nums[key] = 0
        
       for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
                for row in range(r_start, r_start + 3):
                    for column in range(c_start, c_start + 3):
                        tilenum = board[row][column]
                        if tilenum != '.':
                            nums[tilenum] += 1
                if any(y > 1 for y in nums.values()):
                    return False
                for key in nums: nums[key] = 0

       return True