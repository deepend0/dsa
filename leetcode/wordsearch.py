#79. Word Search
from typing import List

from collections import deque

class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		dirs = [(0,1),(-1,0),(0,-1),(1,0)]

		l = len(word)
		m = len(board)
		if m == 0:
			return False
		n = len(board[0])

		visited_stack = deque()
		cur_level = -1
		for i in range(m):
			for j in range(n):
				to_visit = deque([(i,j,0)])
				#print("(i,j)", i,j)
				#print("board", board)
				while to_visit:
					cur_visit = to_visit.pop()
					#print("cur_level", cur_level, "cur_visit_level", cur_visit[2])
					while cur_level >= cur_visit[2]:
						v = visited_stack.pop()
						#print("v", v)
						board[v[0]][v[1]] = v[2]
						cur_level -= 1
					#print("visited_stack", visited_stack, "to_visit", to_visit, "cur_level", cur_level)
					#print("cur_visit", cur_visit, "letters", board[cur_visit[0]][cur_visit[1]], word[cur_visit[2]])
					if board[cur_visit[0]][cur_visit[1]] == word[cur_visit[2]]:
						cur_level = cur_visit[2]
						visited_stack.append((cur_visit[0], cur_visit[1], board[cur_visit[0]][cur_visit[1]]))
						board[cur_visit[0]][cur_visit[1]] = "#"
						#print("match")
						if cur_visit[2] == l - 1:
							return True
						else:
							for d in dirs:
								if -1 < cur_visit[0] + d[0] < m and -1 < cur_visit[1] + d[1] < n:
									to_visit.append((cur_visit[0] + d[0], cur_visit[1] + d[1], cur_visit[2] + 1))

		return False


s = Solution()
#print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
#print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
#print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
#print(s.exist([], "ABCB"))
#print(s.exist([[]], "ABCB"))
#print(s.exist([["D","A", "L", "S"],["A", "K", "R", "A"], ["R","K","A","R"],["K","L","A","T"],["A", "L", "K", "A"]], "DALSARKARKARTALKALKA"))
#print(s.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], "AAAAAAAAAAAAABB"))
#print(s.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","A","B"]], "AAAAAAAAAAAAABB"))
#print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))

class Solution2:
	def __init__(self):
		self.dirs = [(0,1),(-1,0),(0,-1),(1,0)]
		self.m = 0
		self.n = 0
		self.l = 0
		self.board = None
		self.word = None

	def exist(self, board: List[List[str]], word: str) -> bool:
		self.m = len(board)
		if self.m == 0:
			return False
		self.n = len(board[0])
		self.l = len(word)
		self.board = board
		self.word = word

		for i in range(self.m):
			for j in range(self.n):
				if self.exists_dfs(i, j, 0):
					return True
		return False

	def exists_dfs(self, x, y, i):

		if 0 <= x < self.m and 0 <= y < self.n and self.board[x][y] == self.word[i]:
			if i == self.l - 1:
				return True
			else:
				c = self.board[x][y]
				self.board[x][y] = ""
				for d in self.dirs:
					if self.exists_dfs(x + d[0], y + d[1], i + 1):
						return True
				self.board[x][y] = c

		return False


s2 = Solution2()

print(s2.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(s2.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(s2.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(s2.exist([], "ABCB"))
print(s2.exist([[]], "ABCB"))
print(s2.exist([["D","A", "L", "S"],["A", "K", "R", "A"], ["R","K","A","R"],["K","L","A","T"],["A", "L", "K", "A"]], "DALSARKARKARTALKALKA"))
print(s2.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], "AAAAAAAAAAAAABB"))
print(s2.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","A","B"]], "AAAAAAAAAAAAABB"))
print(s2.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))

import time
start = time.time()
print(s.exist([["A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","B","A","A","A","A","A","A"],["A","A","A","A","B","A","A","A","A","A","A","A"]], "AAAAAAAAAAAAABB"))
end = time.time()
print("time ", end - start)


start = time.time()
print(s2.exist([["A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","B","A","A","A","A","A","A"],["A","A","A","A","B","A","A","A","A","A","A","A"]], "AAAAAAAAAAAAABB"))
end = time.time()
print("time ", end - start)
