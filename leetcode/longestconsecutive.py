# 128. Longest Consecutive Sequence
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = dict()
        mins = set()

        for num in nums:
            if num in cons:
                continue
            if num - 1 in cons:
                cons[num-1] = num
            else:
                mins.add(num)

            if num + 1 in cons:
                mins.remove(num + 1)
                cons[num] = num + 1
            else:
                cons[num] = None

        long_seq = 0
        for m in mins:
            seq = 0
            while m is not None:
                seq += 1
                m = cons[m]
            if seq > long_seq:
                long_seq = seq

        return long_seq

s = Solution()
print(s.longestConsecutive([4,1,10,15,12,2,7,11,3,13,5,6,16]))
print(s.longestConsecutive([1,2,3,4,5,6,7]))
print(s.longestConsecutive([1,3,5,7,9,11,13]))
print(s.longestConsecutive([7,6,5,4,3,2,1]))
print(s.longestConsecutive([]))
print(s.longestConsecutive([4,1,1,10,10,15,12,2,2,7,11,3,13,5,11,13,6,6,16]))
print(s.longestConsecutive([7,7,6,6,5,5,4,4,3,3,2,2,1,1]))
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))