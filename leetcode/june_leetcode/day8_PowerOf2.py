#fastest 12 ms
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        i = 2
        while i <= n:
            if i == n:
                return True
            i *= 2
        return False

#16 ms
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n and not (n & (n - 1)))
        
#30 ms
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>-1:
            if bin(n).count('1')==1:
                return True
            else:
                return False
        else:
            return False
