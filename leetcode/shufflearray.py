# 384. Shuffle an Array
from typing import List
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums
        

    def shuffle(self) -> List[int]:
        nums_copy = list(self.nums)
        len_nums = len(nums_copy)
        for i in range(len_nums - 1):
            j = random.randint(i, len_nums - 1)
            nums_copy[j], nums_copy[i] = nums_copy[i], nums_copy[j]

        return nums_copy

s = Solution([1,2,3,4,5,6,10])
print(s.shuffle())
print(s.shuffle())
print(s.shuffle())
print(s.shuffle())
print(s.shuffle())