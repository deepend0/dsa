from typing import List

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        abcount = dict()
        bcount = dict()
        cdcount = dict()
        dcount = dict()
        
        for i in D:
            if i not in dcount:
                dcount[i] = 1
            else:
                dcount[i] += 1
        
        for i in C:
            for k,v in dcount.items():
                if i+k not in cdcount:
                    cdcount[i+k] = v
                else:
                    cdcount[i+k] += v
                    
        for i in B:
            if i not in bcount:
                bcount[i] = 1
            else:
                bcount[i] += 1
        
        for i in A:
            for k,v in bcount.items():
                if i+k not in abcount:
                    abcount[i+k] = v
                else:
                    abcount[i+k] += v
        
        count = 0
        for k,v in abcount.items():
            if -1 * k in cdcount:
                count += v * cdcount[-1*k]
                    
        return count
            
s = Solution()
A = [1, 2]
B = [-2,-1]
C = [-1, 2]
D = [0, 2]

print(s.fourSumCount(A,B,C,D))
