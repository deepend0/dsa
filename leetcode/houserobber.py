#198. House Robber

from typing import List

class Solution:
	 def rob(self, nums: List[int]) -> int:

	 	vals = [0] * len(nums)
	 	vals[0] = nums[0]
	 	if len(nums) > 1:
		 	vals[1] = max(nums[0], nums[1])
		 	for i in range(2, len(nums)):
		 		vals[i] = max(vals[i-1], vals[i-2] + nums[i])

	 	return vals[-1]

s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
print(s.rob([2]))