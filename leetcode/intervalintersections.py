#986. Interval List Intersections

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        intersections = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][1] and firstList[i][1] >= secondList[j][0]:
                intersection = [max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])]
                intersections.append(intersection)
                
            i_inc = firstList[i][1] <= secondList[j][1]
            j_inc = secondList[j][1] <= firstList[i][1]
            if i_inc:
                i += 1
            if j_inc:
                j += 1

        return intersections


s = Solution()

print(s.intervalIntersection([[1,3], [4,5], [7,9], [13,14], [17,19]], [[2,6], [10,12], [13,14], [16,18]]))
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))

print(s.intervalIntersection([],[]))
print(s.intervalIntersection([[1,2]],[[3,4]]))
