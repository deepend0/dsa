#190. Reverse Bits
#190. Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        r = n & 0x80000000
        for i in range(31):
            n = n<<1
            r = r>>1
            r |= n & 0x80000000
        return r

s = Solution()
print(s.reverseBits(1)) # 2^31
print(s.reverseBits(0x80000000)) # 1
print(s.reverseBits(3)) # 2^31 + 2^30
print(s.reverseBits(0xC0000000)) # 3

