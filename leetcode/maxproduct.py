# 152. Maximum Product Subarray

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    	maxProduct = nums[0]
    	curProduct = 1
    	for i in range(len(nums)):
    		curProduct *= nums[i]
    		if curProduct > maxProduct:
    			maxProduct = curProduct
    		if curProduct == 0:
    			curProduct = 1

    	curProduct = 1
    	for i in range(len(nums)-1, -1, -1):
    		curProduct *= nums[i]
    		if curProduct > maxProduct:
    			maxProduct = curProduct
    		if curProduct == 0:
    			curProduct = 1

    	return maxProduct

s = Solution()
print(s.maxProduct([1,2,3,4,5,6])) #720
print(s.maxProduct([5,4,3,-1,3,2,1])) #60
print(s.maxProduct([3,2,1,-1,5,4,3])) #60
print(s.maxProduct([5,-5,4,-4,3,-3])) #1200
print(s.maxProduct([-3,5,-5,4,-4,3])) #1200
print(s.maxProduct([5,-5,4,-4,0,3,-3,2,-2,0,-6,6,-5])) #400
print(s.maxProduct([3,-3,2,-2,0,-6,6,-5,0,5,-5,4,-4])) #400
print(s.maxProduct([-5])) #-5
print(s.maxProduct([-5,0,-4,0,-3,0,-2,0])) #0
print(s.maxProduct([2,3,-2,4])) #6
print(s.maxProduct([-2,0,-1])) #0
print(s.maxProduct([0,2])) #2
print(s.maxProduct([0,2,0,6,0])) #6