import re

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        letArr = re.split("\d+", S)
        if letArr and letArr[-1] == '':
            letArr = letArr[:-1]
        nums = re.split("[a-zA-Z]+", S)[1:]
        for i in range(len(nums)):
            if nums[i] == '':
                nums[i] = 1
            else:
                numnum = 1
                for j in range(len(nums[i])):
                    numnum *= int(nums[i][j])
                nums[i] = numnum
        parts = []

        for i in range(len(letArr)):
            let = letArr[i]
            num = int(nums[i])

            prevPartLen = 0
            if len(parts) > 0:
                prevPartLen = parts[-1][1]

            partSegLen = prevPartLen + len(let)
            parts.append((partSegLen, partSegLen * num))

        #print(parts)

        kpart = None
        kparti = -1
        for i in range(len(parts)):
            part = parts[i]
            if part[1] >= K:
                kpart = part
                kparti = i
                K = ((K-1) % kpart[0])+1
                break

        #print(kpart, kparti, K)
        while kparti > 0 and parts[kparti - 1][1] >= K:
            #print(kpart, kparti, K)
            kparti -= 1
            kpart = parts[kparti]
            K = ((K-1) % kpart[0])+1

        #print(kpart, kparti, K)
        kpartj = K-1
        if kparti > 0:
            kpartj -= parts[kparti-1][1]

        #print(kparti, kpartj)
        return letArr[kparti][kpartj]




s = Solution()
print(s.decodeAtIndex("abc2cde3fgh4", 5))
print(s.decodeAtIndex("abc2cde3fgh4", 19))
print(s.decodeAtIndex("abc2cde3fgh4", 25))
print(s.decodeAtIndex("haha22", 5))
print(s.decodeAtIndex("leet2code3", 10))
print(s.decodeAtIndex("a2345678999999999999999", 1))
print(s.decodeAtIndex("abc", 1))
print(s.decodeAtIndex("a2b3c4d5e6f7g8h9", 3))
print(s.decodeAtIndex("a2b3c4d5e6f7g8h9", 9))

print(s.decodeAtIndex("vzpp636m8y", 2920))
print(s.decodeAtIndex("h5xk8ar9s222v93y22w2", 311373))


def decodeAtIndex(S, K):
    lens, n = [0], len(S)
    for c in S:
        if c.isdigit():
            lens.append(lens[-1] * int(c))
        else:
            lens.append(lens[-1] + 1)

    for i in range(n, 0, -1):
        K %= lens[i]
        if K == 0 and S[i - 1].isalpha():
            return S[i - 1]


print(decodeAtIndex("h5xk8ar9s222v93y22w2", 311373))