class Solution {
public:
    int maxProfit(vector<int>& price) {
      int n=price.size();
        


// Function to find maximum profit that can be earned by buying and
// selling shares any number of times

	// store maximum profit gained
	int profit = 0;

	// initialize local minimum to first element's index
	int j = 0;

	// start from second element
	for (int i = 1; i < n; i++)
	{
		// update local minimum if decreasing sequence is found
		if (price[i - 1] > price[i]) {
			j = i;
		}

		// sell shares if current element is peak
		// i.e. (previous <= current > next)
		if (price[i - 1] <= price[i] &&
			(i + 1 == n || price[i] > price[i + 1]))
		{
			profit += (price[i] - price[j]);
			//printf("Buy on day %d and sell on day %d\n", j + 1, i + 1);
		}
	}

	return profit;

  
        
        
        
    }
};