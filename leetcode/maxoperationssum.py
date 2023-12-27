from typing import List
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] += 1
        print(numMap)
        numOp = 0
        for num in numMap.keys():
            while numMap[num] > 0:
                numMap[num] -= 1

                pairNum = k - num
                if pairNum in numMap and numMap[pairNum] > 0:
                    numOp += 1
                    numMap[pairNum] -= 1
                else:
                    break

        return numOp


s = Solution()
print(s.maxOperations([1,2,3,4], 5))
print(s.maxOperations([3,1,3,4,3], 6))
print(s.maxOperations([3,1,3,4,3], 9))

