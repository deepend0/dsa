# 153. Find Minimum in Rotated Sorted Array
from typing import List

class Solution:
	def findMin(self, nums: List[int]) -> int:
		if len(nums) == 0:
			return -1

		if nums[0] <= nums[-1]:
			return nums[0]

		l, r = 0, len(nums) - 1
		while l <= r:
			m = int((l + r) / 2)
			if nums[m] < nums[m-1]:
				return nums[m]
			if nums[0] <= nums[m]:
				l = m + 1
			else:
				r = m - 1

s = Solution()
print(s.findMin([1,2,3,4,5,6,7]))
print(s.findMin([4,5,6,7,1,2,3]))
print(s.findMin([9,1,2,3,4,5,6,7,8]))
print(s.findMin([]))
print(s.findMin([3]))