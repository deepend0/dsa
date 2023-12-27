from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        dp = [[0 for __ in range(ncols)] for _ in range(nrows)]

        dp[nrows-1][ncols-1] = grid[nrows-1][ncols-1]
        for i in range(nrows-2, -1, -1):
            dp[i][ncols-1] = grid[i][ncols-1] + dp[i+1][ncols-1]
        for i in range(ncols-2, -1, -1):
            dp[nrows-1][i] += grid[nrows-1][i] + dp[nrows-1][i+1]

        for i in range(nrows-2, -1, -1):
            for j in range(ncols-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(s.minPathSum([[1,2,3],[4,5,6]]))
