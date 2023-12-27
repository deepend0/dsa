# 300. Longest Increasing Subsequence

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []

        for num in nums:
            l = 0
            r = len(seq) - 1
            while l <= r:
                m = (l + r) // 2
                if seq[m] < num:
                    l = m + 1
                else:
                    r = m - 1

            if l >= len(seq):
                seq.append(num)
            else:
                seq[l] = num

        return len(seq)


s = Solution()
print(s.lengthOfLIS([2,5,8,10,7]))
print(s.lengthOfLIS([6,7,8,9,1,2,3,4,5]))
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS([7,7,7,7,7,7,7]))
print(s.lengthOfLIS([0,1,0,3,2,3]))



