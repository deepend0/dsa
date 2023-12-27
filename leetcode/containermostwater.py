#11. Container With Most Water

from typing import List

class Solution:
    def maxArea(self, h: List[int]) -> int:
        i = 0
        j = len(h) - 1
        area = 0
        while i < j:
            h_i = h[i]
            h_j = h[j]
            min_h = min(h_i, h_j)
            n_area = (j - i) * min_h
            if n_area > area:
                area = n_area

            if min_h == h_i:
                while i < len(h) and h[i] <= h_i :
                    i += 1
            if min_h == h_j:
                while j > -1 and h[j] <= h_j:
                    j -= 1

        return area

s = Solution()

print(s.maxArea([5,10,4,3,9,5]))
print(s.maxArea([2,7,4,2,6,3]))
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
