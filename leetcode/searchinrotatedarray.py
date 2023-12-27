# 33. Search in Rotated Sorted Array
from typing import List

class Solution:
	def search(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums) - 1

		i = -1
		while l <= r:
			m = int((l + r) / 2)
			if nums[m] == target:
				i = m
				break
			if nums[0] <= nums[m]:
				if nums[m] < target:
					l = m + 1
				else:
					if nums[0] > target:
						l = m + 1
					else:
						r = m - 1
			else:
				if nums[m] > target:
					r = m - 1
				else:
					if nums[-1] < target:
						r = m - 1
					else:
						l = m + 1

		return i


s = Solution()

print(s.search([6,7,8,9,12,3,4], 12))
print(s.search([6,7,8,9,12,3,4], 4))
print(s.search([6,7,8,9,12,3,4], 7))
print(s.search([6,7,8,9,12,3,4], 13))
print(s.search([8,12,1,2,3,4,5], 1))
print(s.search([8,12,1,2,3,4,5], 4))
print(s.search([8,12,1,2,3,4,5], 12))
print(s.search([8,12,1,2,3,4,5], 13))
print(s.search([1,2,3,4,5,6], 5))
print(s.search([1], 1))
print(s.search([1], 0))
print(s.search([], 0))
print(s.search([3,1], 1))