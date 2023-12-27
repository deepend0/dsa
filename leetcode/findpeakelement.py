from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1

        return l


s = Solution()

print(s.findPeakElement([1,2,3,4,5,6,7]))
print(s.findPeakElement([1,2,3,4,5,6,7,3]))
print(s.findPeakElement([7,6,5,4,3,2]))
print(s.findPeakElement([1,2,3,4,3,2,5,6,7,8]))
print(s.findPeakElement([1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))
