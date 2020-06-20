        
#dfs
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i+1) for i in range(n)]
        
        def dfs(remainNums, remainK):
            if len(remainNums) == 1:
                return remainNums[0]
            
            div, mod = divmod(remainK-1, factorial(len(remainNums)-1))
            return remainNums[div] + dfs(remainNums[:div] + remainNums[div+1:], mod+1)
        
        return dfs(nums, k)
    
#mathematical approach    
class Solution:   
    def getPermutation(self,N,K):
        n = N-1
        k = K-1
        def findfact(n):
            global fact
            fact =[0]*n
            fact[0] = 1;
            if(n==1): 
                return
            fact[1] = 1;
            for i in range(2,n):
                fact[i] = i*fact[i-1];
        
        global fact
        findfact(N);
        num=[0]*N
        for i in range(N):
            num[i] = i+1;
        ans = "";        
        while(n>=0):     
            nt = k//fact[n];
            kt = k%fact[n];
            ans += (str(num[nt]));
            #it = num[0]
            del num[nt]
            n-=1;
            k = kt;   
        return ans;
        



#fastest
class Solution(object):
    def get_factorial(self, n):
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    def getPermutation(self, n, k):
        # * the symbols that will be permuted
        chars = [str(i) for i in range(1, n + 1)]
        # * total number of permutations for this n
        k -= 1  # * change indexing to 0
        permutations = self.get_factorial(n)
        result = []

        while chars:
            # * get the first digit (range is 0 to n-1)
            digit = n * k // permutations
            result.append(chars[digit])  # * map from digit to a symbol
            del chars[digit]  # * remove that symbol
            # * repeat for next digit with decreased permutations, n and k
            permutations //= n
            k -= digit * permutations
            n -= 1

        return "".join(result)
        
        
