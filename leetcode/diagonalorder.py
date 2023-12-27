from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix and len(matrix) > 0:
            numRows = len(matrix)
            numCols = len(matrix[0])
        else:
            return []
            
        curdir = 0
        dirOffsets = [(-1, 1), (1, -1)]
        curPos = (0, 0)
        dirLimits = [(-1, numCols), (numRows, -1)]
        dirSwitch = [1, 0]
        dirShift = [(0, 1), (1, 0)]
    
        diagElems = [matrix[0][0]]
        
        while curPos[0] < numRows - 1 or curPos[1] < numCols - 1:
            #print(curdir, curPos)
            nextPos = (curPos[0] + dirOffsets[curdir][0], curPos[1] + dirOffsets[curdir][1])
            
            #print("A", curdir, nextPos)
            if nextPos[0] == dirLimits[curdir][0] or nextPos[1] == dirLimits[curdir][1]:
                nextPos = (curPos[0] + dirShift[curdir][0], curPos[1] + dirShift[curdir][1])
                if nextPos[0] == numRows or nextPos[1] == numCols:
                    #print("B", curdir, nextPos)
                    nextPos = (curPos[0] + dirShift[dirSwitch[curdir]][0], curPos[1] + dirShift[dirSwitch[curdir]][1])
                curdir = dirSwitch[curdir]
                #print("C", curdir, nextPos)
            curPos = nextPos
            diagElems.append(matrix[curPos[0]][curPos[1]])
            
        return diagElems
                    
s = Solution()

print(s.findDiagonalOrder([
]))

print(s.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))

print(s.findDiagonalOrder([
 [ 1, 2, 3, 4, 5 ],
 [ 6, 7, 8, 9, 10 ]
]))


print(s.findDiagonalOrder([
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9, 10, 11, 12 ],
 [ 13, 14, 15, 16 ]
]))
