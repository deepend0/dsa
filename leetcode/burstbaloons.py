from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        numse = [1] + nums + [1]
        s = len(numse)

        dp = [[0 for j in range(s)] for i in range(s)]

        for d in range(2, s):
            for l in range(0, s-d):
                r = l+d
                for i in range(l+1, r):
                    dp[l][r] = max(dp[l][r], numse[l] * numse[i] * numse[r] + dp[l][i] + dp[i][r])
        return dp[0][-1]

s = Solution()
print(s.maxCoins([3,1,5,8]))
print(s.maxCoins([1,5]))
print(s.maxCoins([9, 13, 8, 43, 17, 37]))
print(s.maxCoins([9]))
print(s.maxCoins([]))