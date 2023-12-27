# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_regular = ""
        for c in s.lower():
            if c.isalnum():
                s_regular += c

        l = 0
        r = len(s_regular) - 1
        is_palindrome = True
        while l <= r:
            if s_regular[l] != s_regular[r]:
                is_palindrome = False
                break
            l += 1
            r -= 1

        return is_palindrome


s = Solution()
print(s.isPalindrome("Abcdcba"))
print(s.isPalindrome("Avbbnmng"))
print(s.isPalindrome("Abc d,; c!ba"))
print(s.isPalindrome("Abc d,;k c!ba"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(""))
