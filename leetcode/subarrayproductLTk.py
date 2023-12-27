#713. Subarray Product Less Than K
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        num_products = 0
        product = 1
        while r < len(nums):
            product *= nums[r]

            while l <= r and product >= k:
                product //= nums[l]
                l += 1

            num_products += r - l + 1

            r += 1

        return num_products

s = Solution()
print(s.numSubarrayProductLessThanK([10, 200, 3, 5, 8, 2, 5], 100))
print(s.numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3], 19))
