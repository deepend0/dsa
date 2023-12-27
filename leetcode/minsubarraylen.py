# 209. Minimum Size Subarray Sum
from typing import List

class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		len_nums = len(nums)
		min_len = len_nums + 1

		sum = 0
		l = 0
		for r in range(len_nums):
			sum += nums[r]
			
			while sum - nums[l] >= target:
				sum -= nums[l]
				l += 1

			if sum >= target and min_len > r - l + 1:
				min_len = r - l + 1
				

		if min_len == len_nums + 1:
			min_len = 0

		return min_len


s = Solution()

print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(4, [1,4,4]))
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(s.minSubArrayLen(12, [2, 2, 5, 8, 4, 1, 1, 1, 3, 3, 3, 3]))
print(s.minSubArrayLen(11, []))
print(s.minSubArrayLen(11, [11]))