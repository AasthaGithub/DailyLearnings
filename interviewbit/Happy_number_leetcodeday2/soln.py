def isHappy1(num):
        rem = sum = 0;   
        while(num > 0):    
            rem = num%10;    
            sum = sum + (rem*rem);    
            num = num//10;    
        return sum;
class Solution(object):
    
    
    def isHappy(self, num):   
            
        result = num;    

        while(result != 1 and result != 4):    
            result = isHappy1(result);


        if(result == 1):    
            return True   
        elif(result == 4):    
            return False
        """
        :type n: int
        :rtype: bool
        """
        