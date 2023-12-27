from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        while i < len(nums):
            if nums[i] == nums[i-1] == nums[i-2]:
                del nums[i]
            else:
                i += 1

        return len(nums)


sol = Solution()
print(sol.removeDuplicates([1,1,1,2,2,3]))
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))
