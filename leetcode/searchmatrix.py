# 74. Search a 2D Matrix
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        if row > 0: 
            col = len(matrix[0])
        else:
            col = -1
        l, r = 0, row * col - 1

        while l <= r:
            m = (l + r) // 2
            x, y = m // col, m % col

            if matrix[x][y] == target:
                return True

            if matrix[x][y] < target:
                l = m + 1
            else:
                r = m - 1

        return False

s = Solution()

print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(s.searchMatrix([], 13))
print(s.searchMatrix([[]], 13))