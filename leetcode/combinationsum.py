#39. Combination Sum
from typing import List

class Solution:
	def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
		nums.sort()
		combinations = []
		self.combinationSumSub(nums, 0, target, combinations, [])
		return combinations

	def combinationSumSub(self, nums, ci, target, combinations, combination):
		len_num = len(nums)
		for i in range(ci, len_num):
			new_target = target - nums[i]
			if new_target == 0:
				combination.append(nums[i])
				combinations.append(list(combination))
				combination.pop()

			if new_target <= 0:
				break

			combination.append(nums[i])
			self.combinationSumSub(nums, i, new_target, combinations, combination)
			combination.pop()

s = Solution()
print(s.combinationSum([1,2,3,4,5], 5))