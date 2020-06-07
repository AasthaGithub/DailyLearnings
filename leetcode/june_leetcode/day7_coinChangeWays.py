#https://www.geeksforgeeks.org/coin-change-dp-7/

#92 ms bottom up approach
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * (amount);    
        for coin in coins:
            for i in range(amount - coin + 1):
                if dp[i]:
                    dp[i + coin] += dp[i]
        return dp[amount]
        
#200 ms
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0]*(amount+1)
        ways[0] = 1
        for coin in coins:
            for n in range(1, amount+1):  #this could be improved range=from coin to amount +1
                if coin <= n: #proceed only if the coin denomination is less  than equal to amount left
                    ways[n] += ways[n-coin] #n==coin, there's 1 way to change, i.e. ways[0]=1
        return ways[amount]
