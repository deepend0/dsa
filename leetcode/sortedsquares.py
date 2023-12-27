from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqnegs = []
        sqnonnegs = []
        for num in nums:
            if num < 0:
                sqnegs.append(num*num)
            else:
                sqnonnegs.append(num*num)
        sqs = []
        j = 0
        for i in range(len(sqnegs)-1, -1, -1):
            while j < len(sqnonnegs) and sqnegs[i] > sqnonnegs[j]:
                sqs.append(sqnonnegs[j])
                j += 1
            sqs.append(sqnegs[i])
        
        while j < len(sqnonnegs):
            sqs.append(sqnonnegs[j])
            j += 1
                
        return sqs

s = Solution()
print(s.sortedSquares([-7,-3,2,3,11]))