#371. Sum of Two Integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        INT_MAX = 0x7FFFFFFF
        c = 0x00000000
        d = 0x00000000
        mask  = 0x00000001
        summed = 0x00000000
        for i in range(32):
            d = (c ^ a ^ b) & mask
            c = ((a & b) | (a & c) | (b & c)) & mask
            summed |= d
            a >>= 1
            b >>= 1
            summed = self.right_rotate(summed, 1)
        return summed if summed < INT_MAX else ~(summed ^ 0xFFFFFFFF) 

    def right_rotate(self, a: int, d) -> int:
        return (a >> d) | (a << (32-d)) & 0xFFFFFFFF

s = Solution()

print(s.getSum(1,2))

print(s.getSum(3,3))

print(s.getSum(1024, 512))

print(s.getSum(2147483647, 512))

print(s.getSum(-1, -2))
    