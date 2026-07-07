class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rowLen = len(board)
        colLen = len(board[0])

        def dfs(row, col,i):
            if row < 0 or col < 0 or row >= rowLen or col >= colLen or board[row][col] != word[i]:
                return False
            if (row,col) in visited:
                return False
            if i == len(word)-1:
                return True

            visited.add((row,col))
            
            
            res = (dfs(row,col-1, i+1) or 
            dfs(row, col + 1, i+1) or
            dfs(row-1, col, i+1) or
            dfs(row+1,col, i+1))

            visited.remove((row,col))
            return res
        for r in range(rowLen):
            for c in range(colLen):
                if dfs(r,c,0):
                    return True
        return False
            
        