# 76. Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        rc = dict()
        for c in t:
            if c in rc:
                rc[c] += 1
            else:
                rc[c] = 1
        r = len(t)

        b = 0
        e = 0
        bl = 0
        el = 0

        while e < len(s):
            while e < len(s) and r > 0:
                if s[e] in rc:
                    rc[s[e]] -= 1
                    if rc[s[e]] >= 0:
                        r -= 1
                e += 1

            while r == 0:
                if el == 0 or e - b < el - bl:
                    bl = b
                    el = e
                if s[b] in rc:
                    rc[s[b]] += 1
                    if rc[s[b]] > 0:
                        r += 1
                b += 1

        return s[bl:el]


s = Solution()
print(s.minWindow("axyzbc", "abc"))
print(s.minWindow("axyzbcabc", "abc"))
print(s.minWindow("aaaaaabc", "abc"))
print(s.minWindow("axyzbccakbccc", "abc"))
print(s.minWindow("a", "a"))
print(s.minWindow("aa", "ab"))
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("", "ABC"))
print(s.minWindow("AAAAAAAAAAAAAAAAAAA", "AAA"))
print(s.minWindow("cabwefgewcwaefgcf", "cae"))
