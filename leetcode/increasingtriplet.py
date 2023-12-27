from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
            first = None
            second = None

            for num in nums:
                if first is None or num <= first:
                    first = num
                elif second is None or num <= second:
                    second = num
                else:
                    return True

            return False