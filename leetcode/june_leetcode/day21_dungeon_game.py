'''
Traversing from bottom-right to top-left, we calculate how much hp is required to reach the princess from the current cell.

The first step is to calculate how much hp is required to save the princess upon reaching dungeon[m-1][n-1]:
dungeon[i][j] = min(dungeon[i][j], 0) * -1 + 1
For example:
If dungeon[m-1][n-1] == -5, then we need 6 hp.
If dungeon[m-1][n-1] >= 0 then we only need 1 hp.

For every other cell we find the minimum hp required to reach the princess by going either down or right.
We subtract this minimum hp from the current cell's value to find how much hp would be needed to reach the princess from the current cell.
If this value is <=0, we change it to 1 because that means there is an abundance of hp in this cell and our minimum hp can never be <=0.

'''

class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dungeon[i][j] = min(dungeon[i][j], 0) * -1 + 1
                elif i == m-1:
                    dungeon[i][j] = max(dungeon[i][j+1] - dungeon[i][j], 1)
                elif j == n-1:
                    dungeon[i][j] = max(dungeon[i+1][j] - dungeon[i][j], 1)
                else:
                    dungeon[i][j] = max(min(dungeon[i][j+1], dungeon[i+1][j]) - dungeon[i][j], 1)
        return dungeon[0][0]

#lru cache
class Solution:
    def calculateMinimumHP(self, a: List[List[int]]) -> int:
        n = len(a)
        m = len(a[0])       
        # compute path backwards        
        # max valley for path starting at [i][j]       
        @lru_cache(None)
        def recurse(i,j):            
            if i >= n or j >= m:
                return -inf            
            if i == n-1 and j == m-1:
                return min(0, a[i][j])           
            # my score translates all the next points in the path by +score
            return min(0, max(recurse(i+1,j), recurse(i,j+1)) + a[i][j])    
        return -recurse(0,0) + 1
        

#fastest
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0
        
        num_row, num_col = len(dungeon), len(dungeon[0])
        dp = [float('inf')] * num_col
        dp[num_col - 1] = 1
        
        for row in reversed(range(num_row)):
            for col in reversed(range(num_col)):
                if row == num_row - 1 and col == num_col - 1:
                    dp[col] = max(1, 1 - dungeon[row][col])
                elif row == num_row - 1:
                    dp[col] = max(1, dp[col + 1] - dungeon[row][col])
                elif col == num_col - 1:
                    dp[col] = max(1, dp[col] - dungeon[row][col])
                else:
                    dp[col] = max(1, min(dp[col], dp[col + 1]) - dungeon[row][col])
        
        return dp[0]
