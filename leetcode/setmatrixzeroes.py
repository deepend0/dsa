# 73. Set Matrix Zeroes
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_set = set()
        cols_to_set = set()

        k = len(matrix)
        if k > 0:
            l = len(matrix[0])

            for i in range(k):
                for j in range(l):
                    if matrix[i][j] == 0:
                        rows_to_set.add(i)
                        cols_to_set.add(j)

            for i in rows_to_set:
                for j in range(l):
                    matrix[i][j] = 0
            for i in range(k):
                for j in cols_to_set:
                    matrix[i][j] = 0
        return matrix

s = Solution()
print(s.setZeroes([]))
print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(s.setZeroes([[1,0,1],[1,0,1],[1,0,1]]))
print(s.setZeroes([[1,1,1],[1,1,1],[1,1,1]]))
print(s.setZeroes([[0,1,1],[1,1,1],[1,1,0]]))
print(s.setZeroes([[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,0]]))