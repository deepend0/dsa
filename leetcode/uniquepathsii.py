#63. Unique Paths II
from typing import List

class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])

		num_paths = [[0] * n for _ in range(m)]


		if obstacleGrid[m-1][n-1] == 0:
			num_paths[0][0] = 1
		else:
			return 0

		for i in range(1, m):
			if obstacleGrid[m - 1 - i][n-1] == 0:
				num_paths[i][0] = num_paths[i-1][0]
		for i in range(1, n):
			if obstacleGrid[m-1][n-1-i] == 0:
				num_paths[0][i] = num_paths[0][i-1]
		for i in range(1, m):
			for j in range(1, n):
				if obstacleGrid[m-1-i][n-1-j] == 0:
					num_paths[i][j] = num_paths[i-1][j] + num_paths[i][j-1]

		return num_paths[m-1][n-1]


s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(s.uniquePathsWithObstacles([[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]]))
print(s.uniquePathsWithObstacles([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))
print(s.uniquePathsWithObstacles([[0]]))
print(s.uniquePathsWithObstacles([[0,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]]))