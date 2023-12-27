#90. Subsets II

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort() 
        self.subsetsSub(nums, 0, [], subsets)
        return subsets
    
    def subsetsSub(self, nums, i, currentSubset, subsets):
        last_num = None
        for j in range(i, len(nums)):
            if last_num == nums[j]:
                continue
            else:
                last_num = nums[j]
            currentSubset.append(nums[j])
            subsets.append(list(currentSubset))
            if j + 1 < len(nums):
                self.subsetsSub(nums, j+1, currentSubset, subsets)
            currentSubset.pop()


s = Solution()
print(s.subsetsWithDup([1,1,1,1]))
print(s.subsetsWithDup([-1,1,2]))