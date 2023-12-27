from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        lenArr = len(arr)
        if lenArr<3:
            return False
        step = 0
        prevElem = arr[0]
        for i in range(1, lenArr):
            #print("i", i)
            if step == 0:
                #print("s0")
                if prevElem >= arr[i]:
                    return False
                else:
                    step = 1
            elif step == 1: 
                #print("s1")
                if prevElem == arr[i]:
                    return False
                elif prevElem > arr[i]:
                    step = 2
            elif step == 2:
                #print("s2")
                if prevElem <= arr[i]:
                    return False
            prevElem = arr[i]
        if step == 2:
            return True
        else:
            return False
                    
s = Solution()
print(s.validMountainArray([2,1]))
print(s.validMountainArray([3,5,5]))
print(s.validMountainArray([5,2,6]))
print(s.validMountainArray([0,3,2,1]))
print(s.validMountainArray([1,3,2]))