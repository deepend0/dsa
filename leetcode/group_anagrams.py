# 49. Group Anagrams
from typing import List

from collections import defaultdict
class StrHash:
	def __init__(self, _str):
		self._dict = defaultdict(int)
		for c in _str:
			self._dict[c] += 1

	def __eq__(self, other):
		for k in self._dict.keys():
			if self._dict[k] != other._dict[k]:
				return False
		for k in other._dict.keys():
			if self._dict[k] != other._dict[k]:
				return False
		return True

	def __hash__(self):
		hashCode = 0
		for k in self._dict.keys():
			hashCode += ord(k) * self._dict[k]
		return hashCode

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		strHashes = defaultdict(list)

		for _str in strs:
			strHashes[StrHash(_str)].append(_str)

		return strHashes.values()

s = Solution()
print(s.groupAnagrams(["att", "tat", "vase", "vasc", "esav", "tta"]))
print(s.groupAnagrams([]))
print(s.groupAnagrams(["att", "tatt", "vase", "vasc", "esav1", "ttax"]))
print(s.groupAnagrams(["att", "att", "att", "att", "att", "att"]))

