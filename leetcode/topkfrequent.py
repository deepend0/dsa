#347. Top K Frequent Elements
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numfreq = defaultdict(int)
        maxVal = 0
        for num in nums:
            numfreq[num] += 1
            if maxVal < numfreq[num]:
                maxVal = numfreq[num]

        freqnums = [None] * (maxVal + 1)

        for num in numfreq:
            val = numfreq[num]
            if freqnums[val] == None:
                freqnums[val] = []
            freqnums[val].append(num)

        topk = []
        for i in range(maxVal,0,-1):
            if freqnums[i] != None:
                if len(topk) < k:
                    topk += freqnums[i]
                else:
                    break
        return topk

s = Solution()
print(s.topKFrequent([1,1,2,2,3,3,3,5,5,5,5,7,8,8,8], 2))
print(s.topKFrequent([5,3,1,1,1,3,73,1], 2))
