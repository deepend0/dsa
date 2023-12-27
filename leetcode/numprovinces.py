# 547. Number of Provinces
from typing import List

class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		n = len(isConnected)

		num_components = 0
		visited = set()
		for i in range(n):
			if i not in visited:
				num_components += 1
				to_visit = [i]
				while len(to_visit) != 0:
					cur_node = to_visit.pop()
					if cur_node not in visited:
						visited.add(cur_node)
						for j in range(n):
							if isConnected[cur_node][j] == 1 or isConnected[cur_node][j] == "1":
								to_visit.append(j)

		return num_components


s = Solution()
print(s.findCircleNum([[[1,1,0],[1,1,0],[0,0,1]]]))
print(s.findCircleNum( [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(s.findCircleNum(
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

print(s.findCircleNum([[0,0,0],[0,0,0],[0,0,0]]))

print(s.findCircleNum([[0]]))


print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))