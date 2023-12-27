from typing import List
import heapq
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nrows = len(matrix)
        ncols = len(matrix[0])

        dp = [[0 for __ in range(ncols)] for _ in range(nrows)]

        for i in range(ncols):
            dp[-1][i] = matrix[-1][i]

        for i in range(nrows - 2, -1, -1):
            m = heapq.nsmallest(2, dp[i+1])
            for j in range(ncols):
                dp[i][j] = matrix[i][j] + (m[0] if dp[i+1][j] != m[0] else m[1])

        return min(dp[0])

s = Solution()
print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
