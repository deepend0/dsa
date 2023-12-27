from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount+1)]

        dp[0] = 0

        for i in range(1, amount+1):
            numcoins = None

            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    if numcoins is None or numcoins > dp[i - coin]:
                        numcoins = dp[i - coin]

            if numcoins is not None:
                dp[i] = numcoins + 1

        return dp[-1]

s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([1,2,5], 10))
print(s.coinChange([1], 0))
print(s.coinChange([1], 1))
print(s.coinChange([1], 2))
