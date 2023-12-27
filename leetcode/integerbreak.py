#343. Integer Break

class Solution:
    def integerBreak(self, n: int) -> int:
        sq3 = n // 6
        rem = n % 6

        exp3 = 0
        exp2 = 0
        if sq3 > 0:
            exp3 = 2 * sq3
            if rem == 1:
                exp3 -= 1
                exp2 = 2
            elif rem == 2:
                exp2 = 1
            elif rem == 3:
                exp3 += 1
            elif rem == 4:
                exp2 = 2
            elif rem == 5:
                exp2 = 1
                exp3 += 1
        else:
            if rem == 3:
                exp2 = 1
            elif rem == 4:
                exp2 = 2
            elif rem == 5:
                exp2 = 1
                exp3 = 1

        return pow(2,exp2) * pow(3,exp3)

s = Solution()
print(s.integerBreak(2)) #1
print(s.integerBreak(3)) #2
print(s.integerBreak(4)) #4
print(s.integerBreak(5)) #6
print(s.integerBreak(6)) #9
print(s.integerBreak(19)) #972
print(s.integerBreak(26)) #13122
print(s.integerBreak(33)) #177147
print(s.integerBreak(16)) #324
print(s.integerBreak(47)) #28697814

