from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        subarrays = {subarray[0]: subarray for subarray in pieces}

        i = 0
        while i < len(arr):
            if arr[i] in subarrays:
                subarray = subarrays[arr[i]]
                for j in range(len(subarray)):
                    if arr[i] != subarray[j]:
                        return False
                    i += 1
            else:
                return False

        return True


s = Solution()
print(s.canFormArray([85], [[85]]))
print(s.canFormArray([15,88], [[88],[15]]))
print(s.canFormArray([49,18,16], [[16,18,49]]))
print(s.canFormArray([91,4,64,78],[[78],[4,64],[91]]))
print(s.canFormArray([1,3,5,7], [[2,4,6,8]]))
print(s.canFormArray([], [[2,4,6,8]]))
