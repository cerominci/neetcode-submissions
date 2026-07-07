class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        islands = 0

        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'
            
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
        return islands
            

        