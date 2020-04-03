vector<vector<int> > Solution::generateMatrix(int n) {
    vector< vector<int> > ans;
    ans.resize(n);
    int i=0,j=0,k=1,count=0;
    for(i=0;i<n;i++)
        ans[i].resize(n,0);
    i=j=0;
    while(count!=(n*n))
    {
        for(;j<n && ans[i][j]==0 && count!=(n*n);j++)
        {
            ans[i][j]=k++;
            count++;
        }
        j--;
        i++;
        for(;i<n && ans[i][j]==0 && count!=(n*n);i++)
        {
            ans[i][j]=k++;
            count++;
        }
        i--;
        j--;
        for(;j>=0 && ans[i][j]==0 && count!=(n*n);j--)
        {
            ans[i][j]=k++;
            count++;
        }
        j++;
        i--;
        for(;i>=0 && ans[i][j]==0 && count!=(n*n);i--)
        {
            ans[i][j]=k++;
            count++;
        }
        i++;
        j++;
    }
    return ans;
   
}
