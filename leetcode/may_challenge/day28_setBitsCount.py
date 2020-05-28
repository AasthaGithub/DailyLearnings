#mine, 96 ms
dp=[-1]*100001
dp[0] = 0
flag_done=0

def dps():        
    global dp, flag_done
    if flag_done==0:
        for i in range(100000):
            dp[i]= dp[i >> 1] + (i & 1)
        flag_done=1

class Solution:
        
    def countBits(self, num: int) -> List[int]:
        global dp
        dps()
        ans=[]
        for i in range(num+1):
            ans.append(dp[i])
        
        return ans

'''
fastest 52 ms
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i - (i & -i)] + 1
        return dp
'''
64 ms
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        for i in range(1, num+1):
            dp[i] = dp[i//2] + (1 if (i%2) else 0)
        return dp

  #logic  
    
    class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
		
        next_pow_2 = 1
        add_index = 0
        result = [0 for i in range(num + 1)]
		
        for i in range(1, num + 1):
            if i == next_pow_2:
                next_pow_2 = next_pow_2 * 2
                add_index = 0
            else:
                add_index += 1
            result[i] = 1 + result[add_index]
        
        return result
