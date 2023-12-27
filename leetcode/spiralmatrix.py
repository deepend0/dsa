from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for j in range(n)] for i in range(n)]

        direct = 0
        lbound = ubound = -1
        rbound = dbound = n
        i = j = 0
        for c in range(n*n):
            matrix[i][j] = c + 1
            if direct == 0:
                if j + 1 == rbound:
                    ubound += 1
                    direct = 1
                    i += 1
                else:
                    j += 1
            elif direct == 1:
                if i + 1 == dbound:
                    rbound -= 1
                    direct = 2
                    j -= 1
                else:
                    i += 1
            elif direct == 2:
                if j - 1 == lbound:
                    dbound -= 1
                    direct = 3
                    i -= 1
                else:
                    j -= 1
            elif direct == 3:
                if i - 1 == ubound:
                    lbound += 1
                    direct = 0
                    j += 1
                else:
                    i -= 1

        return matrix

s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(4))
print(s.generateMatrix(5))
print(s.generateMatrix(0))
