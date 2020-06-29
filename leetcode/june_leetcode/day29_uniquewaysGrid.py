'''

ans = n! / [ k! (n-k)! ]
We don't have to calculate all result because partial n! will be eliminated by k! or (n-k)!.
So we only need to calculate the part that cannot be eliminated.
'''

#TC: O(n), SC:O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n,k=n+m-2,m-1
        count=min(n-k,k)
        up=down=1
        while count>0:
            up*=n
            down*=count
            n-=1
            count-=1
        return up//down
        
#TC: O(n^2), SC:O(n)
'''
cpp
int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        while(--m)
            for(int i=1;i<n;++i)
                dp[i]+=dp[i-1];
        return dp[n-1];
    }
'''

#TC: O(n^2), SC:O(n)
'''
cpp
int uniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n,0));
    for(int i=0;i<n;++i) dp[0][i]=1;
    for(int i=0;i<m;++i) dp[i][0]=1;
    for(int i=1;i<m;++i)
        for(int j=1;j<n;++j)
            dp[i][j]=dp[i-1][j]+dp[i][j-1];
    return dp[m-1][n-1];
}
'''
def uniquePaths(self, col: int, row: int) -> int:
        dp = [[0 for _ in range(col+1)]for _ in range(row+1)]      
        total = 0
        dp[row-1][col-1] = 1
        
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i == row-1 and j == col-1: #Destination
                    continue
                    
                if(dp[i+1][j] > 0 or dp[i][j+1] > 0):
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                
        return dp[0][0]
        
#fastest with dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            grid[0][i] = 1
            
        for i in range(n):
            grid[i][0] = 1
            
        for r in range(1, n):
            for c in range(1, m):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
                
        return grid[n-1][m-1]
