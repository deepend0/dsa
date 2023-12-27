from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        nums = dict();
        for e in time:
            if e%60 not in nums:
                nums[e%60] = 0
            nums[e%60] += 1
        
        count = 0
        
        print(nums)
        for k,v in nums.items():
            if 0 < k < 30:
                if 60 - k in nums:
                    count += nums[60-k]*v
            elif k == 0 or k == 30:
                count += v * (v-1) // 2
        return count
        

s = Solution();
print(s.numPairsDivisibleBy60([30,20,150,100,40,10]))
print(s.numPairsDivisibleBy60([60,60,60,60]))