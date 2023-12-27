class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0]=='0':
            return 0
            
        res = [1]
        
        for i in range(1, len(s)):
            resv = 0
            if s[i] != '0':
                resv = res[i-1]
            if s[i-1] != '0' and int(s[i-1:i+1]) < 27 and (i+1 == len(s) or s[i+1] != '0'):
                
                if i>1:
                    resv += res[i-2]
                else:
                    resv += 1
            res.append(resv)
        return res[-1]
        
s = Solution()
print(s.numDecodings("12"))

print(s.numDecodings("226"))

print(s.numDecodings("272"))

print(s.numDecodings("0"))

print(s.numDecodings("012"))

print(s.numDecodings("10"))

print(s.numDecodings("2101"))

print(s.numDecodings(""))