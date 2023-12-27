class Solution:
    def countVowelStrings(self, n: int) -> int:
        countMatrix = [[0 for j in range(n)] for i in range(5)]
        for i in range(n):
            countMatrix[4][i] = 1
        for i in range(5):
            countMatrix[i][0] = 5 - i
            
        for i in range(1, n):
            for j in range(3, -1, -1):
                count = 0
                for k in range(j, 5):
                    count += countMatrix[k][i-1]
                countMatrix[j][i] = count
                
        for i in range(5):
            print(countMatrix[i])
        return countMatrix[0][n-1]
        
        
s = Solution()
print(s.countVowelStrings(1))
print(s.countVowelStrings(2))
print(s.countVowelStrings(3))
print(s.countVowelStrings(4))
print(s.countVowelStrings(33))