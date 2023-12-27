#1496. Path Crossing

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        pos = (0,0)
        visited.add(pos)
        for p in path:
            if p == "N":
                newp = (pos[0], pos[1] + 1)
            elif p =="E":
                newp = (pos[0] + 1, pos[1])
            elif p =="S":
                newp = (pos[0], pos[1] - 1)
            elif p =="W":
                newp = (pos[0] - 1, pos[1])

            if newp in visited:
                return True
            visited.add(newp)
            pos = newp

        return False


s = Solution()
print(s.isPathCrossing("NNWW"))
print(s.isPathCrossing("NNWWSSEE"))
print(s.isPathCrossing("NNWWSSE"))