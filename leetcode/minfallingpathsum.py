from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nrows = len(matrix)
        ncols = len(matrix[0])

        dp = [[0 for __ in range(ncols)] for _ in range(nrows)]

        for i in range(ncols):
            dp[-1][i] = matrix[-1][i]

        for i in range(nrows-2, -1, -1):
            for j in range(ncols):
                ld = dp[i+1][j-1] if j>0 else 100
                d = dp[i+1][j]
                rd = dp[i+1][j+1] if j<ncols-1 else 100

                dp[i][j] = matrix[i][j] + min(ld, d, rd)

        return min(dp[0])


s = Solution()
print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(s.minFallingPathSum([[-19,57],[-40,-5]]))
print(s.minFallingPathSum([[-48]]))

