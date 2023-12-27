#22. Generate Parentheses

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        if n > 0:
            self.generateParenthesisSub(n, 0, 1, "(", arr)
        return arr

    def generateParenthesisSub(self, n, matched, unmatched, cur, arr):
        if matched == n and unmatched == 0:
            arr.append(cur)
            return

        if matched + unmatched <= n and unmatched > 0:
            self.generateParenthesisSub(n, matched + 1, unmatched - 1, cur + ")", arr)
        if matched + unmatched < n:
            self.generateParenthesisSub(n, matched, unmatched + 1, cur + "(", arr)

s = Solution()

print(s.generateParenthesis(0))
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
print(s.generateParenthesis(5))
