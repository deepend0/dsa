#45. Jump Game II
from typing import List

class Solution_DP:
    def jump(self, nums: List[int]) -> int:
        len_nums = len(nums)
        vals = [1001] * len_nums
        vals[-1] = 0
        for i in range(len_nums - 2 , -1, -1):
            min_val = 1001
            if nums[i] != 0:
                for j in range(i + 1, i + nums[i] + 1):
                    if j >= len_nums:
                        break
                    if vals[j] < min_val:
                        min_val = vals[j]
            if min_val == 1001:
                vals[i] = 1001
            else:
                vals[i] = min_val + 1
        return vals[0]


class Solution:
    def jump(self, nums: List[int]) -> int:
        len_nums = len(nums)
        steps = 0
        i = 0
        while i < len_nums - 1:
            if i + nums[i] >= len_nums - 1:
                i = len_nums - 1
            else:
                max_step = 0
                max_i = i
                for j in range(i+1, i + nums[i] + 1):
                    if nums[j] + j > max_step:
                        max_step = nums[j] + j
                        max_i = j
                if i == max_i:
                    return -1
                i = max_i
            steps += 1
        return steps

s = Solution()
print(s.jump([2,3,1,1,4])) # 2
print(s.jump([2,3,0,1,4])) # 2
print(s.jump([2])) # 0
print(s.jump([2,3])) # 1
print(s.jump([3,2,1])) # 1
print(s.jump([8,7,1])) # 1
print(s.jump([8,10,1])) # 1
print(s.jump([3,4,3,1,0,7,0,3,0,2,0,3])) # 3
print(s.jump([5,9,3,2,1,0,2,3,3,1,0,0])) # 3
print(s.jump([5,9,3,2,1,0,2,3,2,1,0,0])) # -1
