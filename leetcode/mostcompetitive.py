from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = []
        len_nums = len(nums)
        for i in range(len_nums):
            while st and st[-1] > nums[i] and k - len(st) + 1 <= len_nums - i:
                st.pop()
            if len(st) < k:
                st.append(nums[i])
            
        return st
        
s = Solution()
print(s.mostCompetitive([3,5,2,6], 2))
print(s.mostCompetitive([2,4,3,3,5,4,9,6], 4))
