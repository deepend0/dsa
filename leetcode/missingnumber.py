# 268. Missing Number
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsOrd = [-1] * (len(nums) + 1)
        for num in nums:
            numsOrd[num] = 1

        for i in range(len(numsOrd)):
            if numsOrd[i] == -1:
                return i

        return -1

s = Solution()

print(s.missingNumber([3,1,0]))

print(s.missingNumber([1,2,3,4,5,6,7,8,9]))

print(s.missingNumber([8,7,4,2,0,1,6,3]))

print(s.missingNumber([0,1,2,3,5]))

print(s.missingNumber([0,1,2,3,5,4]))