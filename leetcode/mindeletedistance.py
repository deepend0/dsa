# 583. Delete Operation for Two Strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for __ in range(l2 + 1)] for _ in range(l1 + 1)]

        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j], dp[i+1][j], dp[i][j+1])


        return l1 + l2 - dp[-1][-1] * 2


s = Solution()
print(s.minDistance("axbycz", "aprbcx"))
print(s.minDistance("sea", "eat"))
print(s.minDistance("leetcode", "etco"))
