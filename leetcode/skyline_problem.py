# 218. The Skyline Problem

from typing import List

class Solution:
	def getSkyline(self, bs: List[List[int]]) -> List[List[int]]:
		segments = []

		intersect = False

		s = bs[0][0]
		while bs:
			e = bs[0][1]
			h = bs[0][2]
			eis = [0]
			intersect = False
			for i in range(1, len(bs)):
				b = bs[i]
				if s <= b[1] and e >= b[0]:
					if s < b[0]:
						segments.append([s,h])
						s = b[0]
					if e == b[1]:
						eis.append(i)
					else:
						intersect = True
						if e > b[1]:
							e = b[1]
							eis = [i]
					if h < b[2]:
						h = b[2]
				else:
					break

			#print("[s,e]", [s,e,h])
			segments.append([s,h])
			eis.reverse()
			for ei in eis:
				del bs[ei]

			if intersect:
				s = e
			else:
				segments.append([e,0])
				if bs:
					s = bs[0][0]

		for i in range(len(segments)-1,0,-1):
			if segments[i][1] == segments[i-1][1]:
				del segments[i]


		return segments

s = Solution()
print(s.getSkyline([[1,5,5],[2,3,7],[4,7,4]])) #[[1,5],[2,7],[3,5],[5,4],[7,0]]
print(s.getSkyline([[1,6,4],[2,4,7],[3,7,5]])) #[[1,4],[2,7],[4,5],[7,0]]
print(s.getSkyline([[1,5,5],[6,7,7]])) #[[1,5],[5,0],[6,7],[7,0]]
print(s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])) #[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
print(s.getSkyline([[0,2,3],[2,5,3]])) #[[0,3],[5,0]]

class LineSegments:
	def getLineSegments(self, bs: List[List[int]]) -> List[List[int]]:
		segments = []

		intersect = False
		while bs:
			if intersect:
				s = e
			else:
				s = bs[0][0]
			e = bs[0][1]
			eis = [0]
			intersect = False
			for i in range(1, len(bs)):
				b = bs[i]
				if s < b[1] and e > b[0]:
					if s < b[0]:
						segments.append([s,b[0]])
						s = b[0]

					if e == b[1]:
						eis.append(i)
					else:
						intersect = True
						if e > b[1]:
							e = b[1]
							eis = [i]
				else:
					break

			#print("[s,e]", [s,e])
			segments.append([s,e])
			eis.reverse()
			for ei in eis:
				#print("ei", ei, "bs", bs)
				del bs[ei]

		return segments

s = LineSegments()
#print("result: ",s.getLineSegments([[1,2]])) #[[1, 2]
#print("result: ",s.getLineSegments([[1,5],[2,4],[3,6]])) #[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
#print("result: ",s.getLineSegments([[1,3],[2,5],[4,6]])) #[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
#print("result: ",s.getLineSegments([[1,3],[5,7]])) #[[1,3],[5,7]]
#print("result: ",s.getLineSegments([[1,5],[1,5],[2,4],[3,4],[3,6]])) #[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
#print("result: ",s.getLineSegments([[1,3],[1,3],[5,7],[5,7]])) #[[1,3],[5,7]]