#740. Delete and Earn

from typing import List
from collections import defaultdict

class Solution:
	def deleteAndEarn(self, nums: List[int]) -> int:
		min_num = min(nums)
		max_num = max(nums)
		num_gain = defaultdict(int)
		for num in nums:
			num_gain[num] += num

		len_nums = max_num - min_num + 1
		vals = [0] * len_nums
		vals[0] = num_gain[min_num]
		if len_nums > 1:
			vals[1] = max(num_gain[min_num + 1], num_gain[min_num])
			for i in range(2, len_nums):
				num = i + min_num
				vals[i] = max(num_gain[num] + vals[i-2], vals[i-1])

		return vals[-1]

s = Solution()
print(s.deleteAndEarn([2,2,3,3,3,3,4,4]))
print(s.deleteAndEarn([2,2,3,3,3,3,4,4,4]))
print(s.deleteAndEarn([2,2,3,3,3,3,4,4,6,6,6]))
print(s.deleteAndEarn([3,4,2]))
print(s.deleteAndEarn([2,2,3,3,3,4]))
print(s.deleteAndEarn([2]))
