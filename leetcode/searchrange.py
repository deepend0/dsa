from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        range_indexes = [-1,-1]

        l,r,m = 0, len(nums)-1, 0
        while l<=r:
            m = int((l + r) / 2)
            if nums[m] == target:
                range_indexes[0] = m
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) / 2
        
        l,r = m, len(nums)-1
        while l<=r:
            m = int((l + r) / 2)
            if nums[m] == target:
                range_indexes[1] = m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return range_indexes


s = Solution()

print(s.searchRange([5,7,7,8,8,10], 8))

print(s.searchRange([5,7,7,8,8,10], 9))

print(s.searchRange([8,8,8,8,8,8,8], 8))

print(s.searchRange([1,2,3,8,8,8,8,8,8,10], 8))

print(s.searchRange([], 8))

print(s.searchRange([8], 8))
