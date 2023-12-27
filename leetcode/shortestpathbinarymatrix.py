# 1091. Shortest Path in Binary Matrix
from typing import List
class Solution:
	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		offsets = [(1,0), (1,-1), (0,-1), (-1, -1), (-1, 0), (-1, 1), (0,1), (1,1)]
		m = len(grid)
		n = len(grid[0])
		to_visit = []
		if grid[0][0] == 0:
			to_visit.append((0,0,1))

		visited = set()
		while to_visit:
			cur_node = to_visit.pop(0)
			cur_pos = (cur_node[0], cur_node[1])
			if cur_pos not in visited:
				if cur_pos[0] == m-1 and cur_pos[1] == n - 1:
					return cur_node[2]
				visited.add(cur_pos)
				for offset in offsets:
					new_node = (cur_node[0] + offset[0], cur_node[1] + offset[1], cur_node[2] + 1)
					new_pos = (new_node[0], new_node[1])
					if 0 <= new_pos[0] < m and 0 <= new_pos[1] < n and grid[new_pos[0]][new_pos[1]] == 0:
						to_visit.append(new_node)

		return -1

s = Solution()
print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
print(s.shortestPathBinaryMatrix([[0,1,0,0],[1,0,1,0],[0,1,1,1],[0,1,0,0]]))
print(s.shortestPathBinaryMatrix([[0,1,0,0],[1,0,1,0],[0,1,0,0],[0,1,0,0]]))