from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        numEligible = 0
        lenF = len(flowerbed)
        numBlock = 0
        for i in range(0, lenF):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == lenF-1 or flowerbed[i+1] == 0):
                    numBlock += 1

                if (i < lenF - 2 and flowerbed[i+2] == 1) or i == lenF - 1:
                        numEligible += (numBlock + 1) // 2
                        numBlock = 0

        #print(numEligible)

        if numEligible >= n:
            return True
        else:
            return False

s = Solution()
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(s.canPlaceFlowers([0, 0, 1, 0, 0, 0, 0, 1], 2))
print(s.canPlaceFlowers([0, 0, 1, 0, 0, 0, 0, 1], 3))
print(s.canPlaceFlowers([1, 0, 1, 0, 1], 0))

print(s.canPlaceFlowers([1,0,0,0,1,0,0], 2))