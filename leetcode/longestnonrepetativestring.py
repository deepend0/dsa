#3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	max_len = 0

    	len_s = len(s)

    	l = 0
    	r = 0

    	chars = set()
    	while r < len_s:
    		while r < len_s and s[r] not in chars:
    			chars.add(s[r])
    			r += 1

    		if len(chars) > max_len:
    			max_len = len(chars)

    		if r < len_s:
    			while s[l] != s[r]:
    				chars.remove(s[l])
    				l += 1
    			chars.remove(s[l])
    			l += 1

    	return max_len

s = Solution()
print(s.lengthOfLongestSubstring("a"))
print(s.lengthOfLongestSubstring("abcabcbbca"))
print(s.lengthOfLongestSubstring("aaaaaaaaaa"))
print(s.lengthOfLongestSubstring("abcdefghij"))
print(s.lengthOfLongestSubstring("aaaaabcdeaaaa"))
print(s.lengthOfLongestSubstring("abcdeeeeeeeeedcba"))
print(s.lengthOfLongestSubstring("pwwkew"))


