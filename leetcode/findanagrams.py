# 438. Find All Anagrams in a String
from typing import List
from collections import defaultdict

class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		p_dict = defaultdict(int)
		for c in p:
			p_dict[c] += 1

		indexes = []

		p_len = len(p)
		s_len = len(s)
		
		if s_len >= p_len:
			sw_dict = defaultdict(int)
			for i in range(p_len):
				sw_dict[s[i]] += 1
			if sw_dict == p_dict:
				indexes.append(0)

			for i in range(1, s_len - p_len + 1):
				sw_dict[s[i - 1]] -= 1
				if sw_dict[s[i - 1]] == 0:
					del sw_dict[s[i - 1]]
				sw_dict[s[i - 1 + p_len]] += 1
				if sw_dict == p_dict:
					indexes.append(i)

		return indexes

s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))
print(s.findAnagrams("a", "ab"))
print(s.findAnagrams("", "ab"))