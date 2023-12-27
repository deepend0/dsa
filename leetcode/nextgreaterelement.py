class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digitsN = self.digits(n)
        
        #print(digitsN)
        permResult = self.nextPermutation(digitsN)
        if permResult is not None:
            res = self.n(digitsN)
            if res < 0x7fffffff:
                return res
            else:
                return -1
        else:
            return -1
        
    def digits(self, n: int):
        digits = []
        
        while n >= 1:
            digits.append(n%10)
            n //= 10
        digits.reverse()
        return digits
    

    def n(self, digits):
        n = 0
        
        for d in digits:
            n *= 10
            n += d
        return n
        
    def nextPermutation(self, perm):
        
        curi = perm[-1]
        avails = [curi]
        i = -2
        while -1 * i <= len(perm) and avails[-1] <= perm[i]:
            curi = perm[i]
            avails.append(curi)
            i -= 1
        
        print(perm, avails, i, curi)
        if -1 * i > len(perm):
            return None
        
        curi = perm[i]
            
        j=-1
        while (-1*j - 1) < len(avails) and curi<avails[j]:
            j -= 1
            
        perm[i], avails[j+1] = avails[j+1], perm[i]
        #print(i, j+1)
        #print(perm, avails)
        for j in range(len(avails)):
            perm[i + j + 1] = avails[j]
        
        #print(perm, avails)
        
        return perm

s = Solution()
print(s.nextGreaterElement(634527))
#a = [2, 3, 4, 5, 6, 7]
#for i in range(20):
#    s.nextPermutation(a)


#a = 634527
#for i in range(20):
#    a = s.nextGreaterElement(a)
#    print(a)
    
a = 12
a = s.nextGreaterElement(a)
print(a)


a = s.nextGreaterElement(1999999999)
print(a)
a = s.nextGreaterElement(54321)
print(a)


a = s.nextGreaterElement(11)
print(a)

a = s.nextGreaterElement(230241)
print(a)

