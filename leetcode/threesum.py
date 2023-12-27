from typing import List

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		values = set()
		nums_set = dict()
		for i in range(0, len(nums)):
			nums_set[nums[i]] = i

		for i in range(0, len(nums)):
			for j in range(i+1, len(nums)):
				remaining_value = -1 * (nums[i] + nums[j])
				if remaining_value in nums_set:
					remaining_index = nums_set[remaining_value]
					if remaining_index > j:
						vals = [nums[i], nums[j], remaining_value]
						vals.sort()
						values.add(tuple(vals))

		return values


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([]))

print(s.threeSum([-1]))