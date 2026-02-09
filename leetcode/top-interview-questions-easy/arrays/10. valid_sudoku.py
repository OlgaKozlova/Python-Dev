def checkList(lst: List[str]) -> bool:
    smap = {}
    for item in lst:
        if item == '.':
            continue
        else:
            if smap.get(item, None) is not None:
                return False
            else:
                smap[item] = True
    return True
    

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = board
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                item = board[r][c]
                squareIndex = (r // 3) * 3 + (c // 3)
                cols[c].append(item)
                squares[squareIndex].append(item)
        
        result = rows + cols + squares
        
        for sud in result:
            if not checkList(sud):
                return False
        
        return True
                
        