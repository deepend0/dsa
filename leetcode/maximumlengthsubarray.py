#718. Maximum Length of Repeated Subarray

from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        dp = [[0 for __ in range(l2 + 1)] for _ in range(l1 + 1)]

        for i in range(l1):
            for j in range(l2):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = 0

        return max(map(max, dp))

s = Solution()
print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))
print(s.findLength([1,1,1,1,1], [1,1,1,1,1]))
print(s.findLength([1,1,1,1,1], [2,2,2,2,2]))
print(s.findLength([1,2,3,4,8,9,10,11,12, 30,31,32], [30,31,32,10,10,10,1,2,3,4,8]))
