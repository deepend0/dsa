import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            minVal = i
            for j in range(1, int(math.sqrt(i)+1)):
                if minVal > dp[i-j*j]:
                    minVal = dp[i-j*j]
            dp[i] = minVal + 1

        return dp[-1]


s = Solution()
print(s.numSquares(1))
print(s.numSquares(10))
print(s.numSquares(19))
print(s.numSquares(43))
print(s.numSquares(49))
