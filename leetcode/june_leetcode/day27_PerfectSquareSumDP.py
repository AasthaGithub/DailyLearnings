#dp soln

#I/P: 12
#O/P: 3, since 12=(Perfect Square =4)*3

class Solution:
  def Perfectsquares(amount):
        squares=[i*i for i in range(1,int(amount**0.5)+1)]
        ways = [float('inf')]*(amount+1)
        ways[0] = 0
        for coin in reversed(squares):
            for n in range(amount,1,-1):
                if coin <= n: 
                    #proceed only if the coin denomination is less  than equal to amount left
                    ways[n] =min( ways[n-coin]+1 ,ways[n])
                    #n==coin, there's 1 way to change, i.e. ways[0]=1
        return ways[amount]
