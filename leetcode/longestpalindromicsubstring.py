class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens = len(s)
        pals = ""
        lenpals = 0
        for i in range(lens):
            l = r = i
            while l > -1 and r < lens and s[l]==s[r]:
                if lenpals < r - l + 1:
                    pals = s[l:r+1]
                    lenpals = r - l + 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l > -1 and r < lens and s[l]==s[r]:
                if lenpals < r - l + 1:
                    pals = s[l:r+1]
                    lenpals = r - l + 1
                l -= 1
                r += 1
        
        return pals
        
s = Solution()
print(s.longestPalindrome("babad"))
