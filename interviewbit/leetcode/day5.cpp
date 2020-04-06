int maxProfit1(int start, int end,vector<int>& price) {


    

    // If the stocks can't be bought 
    if (end <= start) 
        return 0; 
  
    // Initialise the profit 
    int profit = 0; 
  
    // The day at which the stock 
    // must be bought 
    for (int i = start; i < end; i++) { 
  
        // The day at which the 
        // stock must be sold 
        for (int j = i + 1; j <= end; j++) { 
  
            // If byuing the stock at ith day and 
            // selling it at jth day is profitable 
            if (price[j] > price[i]) { 
  
                // Update the current profit 
                int curr_profit = price[j] - price[i] 
                                  + maxProfit1(start,i-1,price) 
                                  + maxProfit1(j+1,end,price); 
  
                // Update the maximum profit so far 
                profit = max(profit, curr_profit); 
            } 
        } 
    } 
    return profit;} 
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit=0;
        int start=0;
        int end =prices.size()-1;
        profit=maxProfit1(start,end,prices);
        return profit;
    }
};