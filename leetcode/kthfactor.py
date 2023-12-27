import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        sqn = int(math.sqrt(n))

        factors_1 = []
        factors_2 = []

        for i in range(1, sqn + 1):
            if n % i == 0:
                factors_1.append(i)
                if i != n/i:
                    factors_2.append(n // i)

        print(factors_1)
        print(factors_2)

        if k <= len(factors_1):
            return factors_1[k-1]
        elif k <= len(factors_1) + len(factors_2):
            return factors_2[-1*(k-len(factors_1))]
        else:
            return -1


sol = Solution()

print(sol.kthFactor(12, 3))
print(sol.kthFactor(7, 2))
print(sol.kthFactor(4, 4))
print(sol.kthFactor(1, 1))
print(sol.kthFactor(1000, 3))
print(sol.kthFactor(24, 6))
