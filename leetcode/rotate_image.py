# 48. Rotate Image

from typing import List
from math import ceil

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        num_iter = ceil(n/2)

        for i in range(num_iter):
            for j in range(i, n-i-1):
                matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i], matrix[i][j] = matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i]

s = Solution()
m = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(m)
print(m)

m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
s.rotate(m)
print(m)

m = [[1]]
s.rotate(m)
print(m)

m = []
s.rotate(m)
print(m)
