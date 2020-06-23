# DP
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid) -> int:
        '''
        An island is adjacent lands horizontally or vertically like a +
        i.e. not diagonally.
        grid: List[List[str]]
        '''
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # deepth-first search all its neighbors
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            # out of bound or water
            return
        else:
            # turn neighboring lands off
            grid[i][j] = '#'
        # check its horizontal and vertical neighbors
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

grid = [['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0'],]
sol = Solution()
print(sol.numIslands(grid))
