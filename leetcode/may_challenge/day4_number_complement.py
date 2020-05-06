'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
'''


'''
Find the highest power just above N. Basically locate the MSB of N then that number ber would 2^(MSB+1)

Then complement would be:2^(MSB+1)-1-N

This works because:

2^(MSB+1)-1 will have all its bits set till MSB
Subtracting N from it means you are flipping the bits of N without worrying about leading zeroes
e.g - If N=5 , msb=2 (taking it 0 based)
So 2^(msb+1)-1 = 2^3-1 = 7(111)
Complement = 7-5 = 111-101=010
'''



class Solution:
    def findComplement(self, N: int) -> int:
        MSB=0
        for i in range(31):
            x = 1<<i
            if (N & x)>>i ==1:
                MSB=i
        
        return pow(2,MSB+1)-1-N        
