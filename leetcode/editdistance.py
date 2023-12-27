#72. Edit Distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[abs(i-j) for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1

        return dp[-1][-1]


s = Solution()
print(s.minDistance("horse", "ros"))
print(s.minDistance("intention", "execution"))
print(s.minDistance("liberal", "lateral"))

print(s.minDistance("maximilianorodrigez", "gez"))


