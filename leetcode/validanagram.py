# 242. Valid Anagram
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	char_count = defaultdict(int)
    	for c in s:
    		char_count[c] += 1

    	for c in t:
    		char_count[c] -= 1
    		if char_count[c] == 0:
    			del char_count[c]

    	return len(char_count) == 0


s = Solution()
print(s.isAnagram("car", "acr"))

print(s.isAnagram("car", "aacr"))

print(s.isAnagram("caar", "acr"))

print(s.isAnagram("car", "acx"))
