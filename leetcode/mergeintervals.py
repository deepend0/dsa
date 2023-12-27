# 56. Merge Intervals

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                merged_intervals.append(interval)

        return merged_intervals


s = Solution()
print(s.merge([[1,3]]))
print(s.merge([[1,3], [2,4]]))
print(s.merge([[1,4], [2,3]]))
print(s.merge([[1,2], [3,4]]))
print(s.merge([[1,4], [2,5], [6,7], [8, 10], [9,11]]))
print(s.merge([[1,5], [5,7], [8, 10]]))
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))

print(s.merge([[2 ,4], [1,3]]))

print(s.merge([[2,5], [9,11], [8, 10], [1,4], [6,7]]))