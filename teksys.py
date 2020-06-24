'''
Question 2

Given N books numbered from 1 to N. You need to arrange them in N shelves (also numbered from 1 to N). Distance between 2 books is calculated as follows:-
absolute value of (shelve_number_of(book1) - shelve_number_of(book2))
You are also given list P. P is the list of pair of books. You need to arrange books in shelves such that sum of book distance between the books in a pair is minimum.
Print the sum of minimum book distance.
Constraint N <= 30 , length(P)<= (N(N+1))/2

Sample Input
N = 5
P = [ [1,2],[1,3] ,[3,4] ]

Sample Output
3
Explanation
The optimal way to arrange book would be:
[2, 1, 3, 4, 5]
The book distance of pairs in P is:-
[1,2] = abs(2-1) = 1
[1,3] = abs(2-3) = 1
[3,4] = abs(3-4) = 1
sum = 1+1+1 = 3


So breaking the time complexity for Q2, solution in O(n * 2^n) time with dynamic programming.
Iterate on the power set of {1,2,..,N} and examine what is last term, if this is "j" then we know which integers are before j and after j, so we'll know the sign in the abs(p[][0]-p[][1]) terms where one term equals to j.
'''
int optimal_Permutation(int n,vector<vector<int>> P){
    
    unordered_map<int,int> mymap;
    int N=0;
    for(int i=0;i<P.size();i++)
        for(int j=0;j<2;j++)
            if(mymap.count(P[i][j])==0)  mymap[P[i][j]]=N++;
    
    vector<int>H(N,0);
    vector<int>offsets(N,0);
    for(int i=0;i<P.size();i++){
        int x=mymap[P[i][0]];
        int y=mymap[P[i][1]];
        offsets[x]+=(1<<y);
        offsets[y]+=(1<<x);
        H[x]++;
        H[y]++;
    }
    
    int p2=1<<N;
    vector<int> numbits(p2),dp(p2);
    for(int i=1;i<p2;i++)numbits[i]=numbits[i/2]+(i%2);
    dp[0]=0;
    for(int i=1;i<p2;i++){
        int opt=INT_MAX;
        for(int j=0;j<N;j++)
            if((i>>j)&1){
                int cnt=numbits[offsets[j]&i];
                int nbits=numbits[i];
                opt=min(opt,dp[i-(1<<j)]+(cnt-(H[j]-cnt))*(nbits-1));
            }
        dp[i]=opt;
    }
    return dp[p2-1];
}

int main(void){

    cout<<optimal_Permutation(5,{{1,2},{1,3},{3,4}})<<endl;
    cout<<optimal_Permutation(6,{{1,2},{1,5},{1,6},{2,6},{2,5},{2,4}})<<endl;
    cout<<optimal_Permutation(8,{{1,3},{1,4},{1,5},{1,8},{2,3},{2,7},{3,6},{3,8},{4,7},{5,8}})<<endl;
    return 0;
}

// output 3, 9, 17




'''
Question 1
Given an array for integers of size n.
You can perform the following step, any numbers of times:-
Choose any 2 adjacent elements, if they have equal value, you can remove the elems(both the elements) and insert value +1 (only once) in that position. [See sample below]

It is also mention first and last element of the array are also adjacent.

Find the maximum element possible in the array after performing such steps.

Constraint n = 10^5
Sample Input:
[1, 2, 3]
Output:
3
Explanation:-
Max of the array -> 3
(You can not perform steps, since there are no adjacent elements with equal value.)

Sample Input:
[5, 3, 3, 3, 4]
Output:
6
Explanation:
We can perform following steps:-
Step 0 [5, 3, 3, 3, 4]

Merge 3,3 and insert 4
Step 1 [5, 3, 4, 4]

Merge 4,4 and insert 5
Step 2 [5, 3, 5]

Merge 5,5 and insert 6 (It is given first and last elem are adjacent)
Step 3 [6, 3] or [3, 6]

Now, find the max of the array => 6.
'''
