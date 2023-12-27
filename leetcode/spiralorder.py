# 54. Spiral Matrix
from typing import List

class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		m = len(matrix)
		n = len(matrix[0])

		elements = []

		dr = 0
		u = 0
		l = 0
		d = m - 1
		r = n - 1

		while r - l >= 0 and d - u >= 0:
			if dr == 0:
				for i in range(l, r + 1):
					elements.append(matrix[u][i])
				u += 1
				dr = 1

			elif dr == 1:
				for i in range(u, d + 1):
					elements.append(matrix[i][r])
				r -= 1
				dr = 2

			elif dr == 2:
				for i in range(r, l - 1 , -1):
					elements.append(matrix[d][i])
				d -= 1
				dr = 3

			elif dr == 3:
				for i in range(d, u - 1, -1):
					elements.append(matrix[i][l])
				l += 1
				dr = 0

		return elements

class Solution2:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		dr = 0
		m = len(matrix)
		n = len(matrix[0])

		elements = []

		u = 0
		l = 0
		d = m - 1
		r = n - 1

		while r - l > 0 and d - u > 0:
			if dr == 0:
				for i in range(l, r):
					elements.append(matrix[u][i])
				dr = 1

			elif dr == 1:
				for i in range(u, d):
					elements.append(matrix[i][r])
				dr = 2

			elif dr == 2:
				for i in range(r, l, -1):
					elements.append(matrix[d][i])
				dr = 3

			elif dr == 3:
				for i in range(d, u, -1):
					elements.append(matrix[i][l])

				u += 1
				l += 1
				d -= 1
				r -= 1
				dr = 0

		if l == r and d - u > - 1:
			for i in range(u, d + 1):
					elements.append(matrix[i][l])
		elif d == u:
			for i in range(l, r + 1):
					elements.append(matrix[u][i])

		return elements

s = Solution()

print(s.spiralOrder([[1,2,3,4,5,6,7,8,9]]))
print(s.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9]]))
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]))
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9], [10,11,12],[13,14,15]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15

# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# 13 14 15