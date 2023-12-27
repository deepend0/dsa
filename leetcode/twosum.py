# Two Sum
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	elems = { nums[i]:i for i in range(len(nums)) }

    	for i in range(len(nums)):
    		num = nums[i]
    		other = target - num
    		if other in elems and elems[other] != i:
    			return [i, elems[other]]

    	return None

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([4,7,11,15], 8))
print(s.twoSum([4,7,11,4], 8))
print(s.twoSum([4,7,11,4], 18))
print(s.twoSum([4,7,11,4], 19))