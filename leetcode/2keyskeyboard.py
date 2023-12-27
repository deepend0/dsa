class Solution:
    def minSteps(self, n: int) -> int:
        dp = [[n for _ in range(n+1)] for __ in range(n+1)]

        for i in range(n, -1, -1):
            dp[n][i] = 0
        for i in range(n-1, 0, -1):
            for j in range(min(i, n-i), -1, -1):
                v = min(dp[i+j][j], dp[i][i])
                if v < n:
                    dp[i][j] = v + 1
        return dp[1][0]


s = Solution()
print(s.minSteps(1))
print(s.minSteps(3))
print(s.minSteps(4))
print(s.minSteps(8))
print(s.minSteps(1024))



