# 121. Best Time to Buy and Sell Stock
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

    	max_profit = 0
    	min_val = float("inf")

    	for price in prices:
    		if price < min_val:
    			min_val = price
    		else:
    			max_profit = max(price - min_val, max_profit)
    	return max_profit

s = Solution()
print(s.maxProfit([50, 60, 40, 100, 30, 90, 20, 70])) #60
print(s.maxProfit([50, 70, 20, 60])) #40
print(s.maxProfit([50, 100, 20, 60])) #50
print(s.maxProfit([50, 40, 80, 20, 70])) #50
print(s.maxProfit([5,4,3,2,1])) #0
print(s.maxProfit([5,4,3,1,2,1])) #1
