from collections import defaultdict

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        m = 10**9 + 7
        lenstr = len(S)
        dp = [0 for i in range(lenstr+1)]
        dp[0] = 1
        last = defaultdict(int)
        for i in range(lenstr):
            dp[i+1] = (2*dp[i] - last[S[i]]) % m
            last[S[i]] += (dp[i+1]- dp[i]) % m

        return dp[-1]-1


s = Solution()
print(s.distinctSubseqII(""))
print(s.distinctSubseqII("a"))
print(s.distinctSubseqII("aaaaa"))
print(s.distinctSubseqII("abcde"))
print(s.distinctSubseqII("abab"))
print(s.distinctSubseqII("abc"))
print(s.distinctSubseqII("zchmliaqdgvwncfatcfivphddpzjkgyygueikthqzyeeiebczqbqhdytkoawkehkbizdmcnilcjjlpoeoqqoqpswtqdpvszfaksn"))