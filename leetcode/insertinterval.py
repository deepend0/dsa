# 57. Insert Interval
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], interval: List[int]) -> List[List[int]]:
        i = self.binary_search(intervals, interval)

        if i == -1:
            i = 0
            intervals.insert(i, interval)
        else:
            if interval[0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], interval[1])
            else:
                i += 1
                intervals.insert(i, interval)

        j = i + 1
        while j < len(intervals) and intervals[j][0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[i][1], intervals[j][1])
            j += 1

        del intervals[i+1:j]

        return intervals

    def binary_search(self, arr, el):
        l = 0
        r = len(arr) - 1

        last = -1
        while l <= r:
            m = (l + r) // 2
            if el[0] < arr[m][0]:
                r = m - 1
            else:
                last = m
                l = m + 1

        return last

s = Solution()

print(s.binary_search([[3,3], [4,7], [9, 12]], [2,4])) #-1
print(s.binary_search([[1,3]], [2,4])) #0
print(s.binary_search([[1,3], [4,7], [9, 12]], [2,4])) #0
print(s.binary_search([[1,3], [4,7], [9, 12]], [4,6])) #1
print(s.binary_search([[1,3], [4,7], [9, 12]], [6, 8])) #1
print(s.binary_search([[1,3], [4,7], [9, 12]], [10, 12])) #2

print(s.insert([[1,3], [5,7], [9, 12]], [2,4])) #[[1, 4], [5, 7], [9, 12]]
print(s.insert([[1,3], [5,7], [9, 12]], [2,5])) #[[1, 7], [9, 12]]
print(s.insert([[1,3], [5,7], [9, 12]], [2,8])) #[[1, 8], [9, 12]]
print(s.insert([[1,3], [5,7], [9, 12]], [2,10])) #[[1, 12]]
print(s.insert([[3,4], [5,7], [9, 12]], [1,2])) #[[1, 2], [3, 4], [5, 7], [9, 12]]
print(s.insert([[3,4], [5,7], [9, 12]], [1,3])) #[[1, 4], [5, 7], [9, 12]]
print(s.insert([[3,4], [5,7], [9, 12]], [13,14])) #[[3, 4], [5, 7], [9, 12], [13, 14]]
print(s.insert([[1,3],[6,9]], [2,5])) #[[1, 5], [6, 9]]
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) #[[1, 2], [3, 10], [12, 16]]