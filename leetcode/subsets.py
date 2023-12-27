# 78. Subsets
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        self.subsetsSub(nums, 0, [], subsets)
        return subsets
    
    def subsetsSub(self, nums, i, currentSubset, subsets):
        for j in range(i, len(nums)):
            currentSubset.append(nums[j])
            subsets.append(list(currentSubset))
            if j + 1 < len(nums):
                self.subsetsSub(nums, j+1, currentSubset, subsets)
            currentSubset.pop()


s = Solution()
print(s.subsets([1,2,5]))
print(s.subsets([]))
print(s.subsets([1,2,5,7]))