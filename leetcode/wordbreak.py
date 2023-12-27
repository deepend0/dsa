# 139. Word Break

from typing import List

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		found = [False] * (len(s) + 1)
		found[0] = True
		for i in range(len(s)):
			for w in wordDict:
				if found[i + 1 - len(w)]:
					if i + 1 - len(w) >= 0 and s[i + 1 - len(w): i + 1] == w:
						found[i + 1] = True
						break
		return found[-1]


s = Solution()
print(s.wordBreak("leetcode", ["leet","code"]))
print(s.wordBreak("applepenapple", ["apple","pen"]))
print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))