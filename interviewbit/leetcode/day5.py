def maxProfit(prices):
    n=len(prices)
    bought=0
    profit=0
    i=0
    while(i<n):
        temp=0
        if bought==0:
            temp=prices[i]
            while(i+1<n):
                if prices[i]<prices[i+1]:
                    bought=1
                    i+=1
                profit+=prices[i]-temp
        if bought==1:
            if prices[i]<prices[i+1]:
                bought=0
                profit+=prices[i+1]-prices[i]
                i+=1
        
        i+=1
    return profit   
listy=list(map(int,input().split()))
y=maxProfit(listy)
print(y)




class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        bought=0
        profit=0
        i=0
        while(i<n-1):
            temp=0
            if bought==0:
                temp=prices[i]
                while(i+1<n):
                    if prices[i]<prices[i+1]:
                        bought=1
                        i+=1
                    profit+=prices[i]-temp
            if bought==1:
                if prices[i]<prices[i+1]:
                    bought=0
                    profit+=prices[i+1]-prices[i]
        return profit    
                
                
        
        """
        :type prices: List[int]
        :rtype: int
        """



def maxProfit1(price,start,end):    
    if (end <= start): 
        return 0; 

    # Initialise the profit 
    profit = 0; 

    # The day at which the stock 
    # must be bought 
    for i in range(start, end, 1): 

        # The day at which the 
        # stock must be sold 
        for j in range(i+1, end+1): 

            # If byuing the stock at ith day and 
            # selling it at jth day is profitable 
            if (price[j] > price[i]): 

                # Update the current profit 
                curr_profit=price[j]-price[i] +maxProfit1(price,start,i-1)+ maxProfit1(price,j + 1,end); 

                # Update the maximum profit so far 
                profit = max(profit, curr_profit); 

    return profit; 

class Solution(object):
    def maxProfit(self, prices):
        pr=maxProfit1(prices,0,len(prices)-1)
        return pr
   