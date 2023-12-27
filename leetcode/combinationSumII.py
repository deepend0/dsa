# 40. Combination Sum II
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        self.combinationSum2Sub([0] + candidates, target, 0, combinations, [])
        return combinations

    def combinationSum2Sub(self, candidates, target, i, combinations, curCombination):
        new_target = target - candidates[i]
        l = len(candidates)
        if new_target == 0:
            curCombination.append(candidates[i])
            combinations.append(list(curCombination[1:]))
            curCombination.pop()
            return False
        elif new_target < 0:
            return False
        else:
            curCombination.append(candidates[i])
            for j in range(i+1, l):
                if j > i + 1 and candidates[j - 1] == candidates[j]:
                    continue
                cont = self.combinationSum2Sub(candidates, new_target, j, combinations, curCombination)
                if not cont:
                    break

            curCombination.pop()
            return True

s = Solution()
print(s.combinationSum2([2,5,2,1,2], 5))
print(s.combinationSum2([2], 5))
print(s.combinationSum2([2], 2))
print(s.combinationSum2([], 2))