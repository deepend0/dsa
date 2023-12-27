# 47. Permutations II

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutations = []
        self.permuteUnique_Sub(nums, permutations, [])
        return permutations


    def permuteUnique_Sub(self, nums, permutations, permutation):
        len_nums = len(nums)
        if len_nums == 1:
            permutation.append(nums[0])
            permutations.append(list(permutation))
            permutation.pop()
        else:
            prev_num = None
            for i in range(len_nums):
                num = nums[i]
                if num != prev_num:
                    permutation.append(num)
                    self.permuteUnique_Sub(nums[:i] + nums[i+1:], permutations, permutation)
                    permutation.pop()
                    prev_num = num

s = Solution()
print(s.permuteUnique([1,2,1,3]))
print(s.permuteUnique([1,1,2]))