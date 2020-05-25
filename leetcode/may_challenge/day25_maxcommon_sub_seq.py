#fastest 68 ms
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        s = set(A) & set(B)
        A = [a for a in A if a in s]
        B = [b for b in B if b in s]
        m, n = len(A), len(B)
        if m < n:
            A, B, m, n = B, A, n, m
            
        dp = [0]*(m+1)                      # dp[i] in loop j: check up to A[i], B[j] 
        for j in range(n):                  # B[0]..B[j]
            new_dp = dp[:]
            for i in range(m):              # A[0]..A[i]
                if A[i] == B[j]:
                    new_dp[i+1] = dp[i] + 1 # add a new line
                else:
                    new_dp[i+1] = max(dp[i+1], new_dp[i])   # choose the best strategy
            dp = new_dp
            
        return dp[-1]
        
#other soln 2D dp
AasthaMehta

LeetCode

1035. Uncrossed Lines
Description
Hints
Submissions
Discuss
Solution
      
Python by O( m*n ) DP [w/ Graph]
Python by O( m*n ) DP [w/ Graph]
343
VIEWS
7
Last Edit: 2 hours ago

brianchiang_tw
brianchiang_tw
 454
Python by O( m*n ) DP

This is a numerical version of Longest common subsequence like Leetcode # 1143

Illustration and Visualization:

image

Hint:

First, add one dummy -1 to A and B to represent empty list

Then, we define the notation DP[ y ][ x ].

Let DP[y][x] denote the maximal number of uncrossed lines between A[ 1 ... y ] and B[ 1 ... x ]

We have optimal substructure as following:

Base case:
Any sequence with empty list yield no uncrossed lines.

If y = 0 or x = 0:
DP[ y ][ x ] = 0

General case:
If A[ y ] == B[ x ]:
DP[ y ][ x ] = DP[ y-1 ][ x-1 ] + 1

Current last number is matched, therefore, add one more uncrossed line

If A[ y ] =/= B[ x ]:
DP[ y ][ x ] = Max( DP[ y ][ x-1 ], DP[ y-1 ][ x ] )

Current last number is not matched,
backtrack to A[ 1...y ]B[ 1...x-1 ], A[ 1...y-1 ]B[ 1...x ]
to find maximal number of uncrossed line

Implementation by 2D dynamic programming:

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        # padding one dummy -1 to represent empty list
        A = [ -1 ] + A
        B = [ -1 ] + B
        
        h, w = len(A), len(B)
        dp_table = [ [ 0 for _ in range(w) ] for _ in range(h) ]
        
        
        
        for y in range(1, h):
            for x in range(1, w):
                
                if A[y] == B[x]:
                    # current number is matched, add one more uncrossed line
                    dp_table[y][x] = dp_table[y-1][x-1] + 1
                    
                else:
                    # cuurent number is not matched, backtracking to find maximal uncrossed line
                    dp_table[y][x] = max( dp_table[y][x-1], dp_table[y-1][x] )

                    
        return dp_table[-1][-1]
        
   
#memoisation

 Solution:


    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        

        A = [ -1 ] + A

        B = [ -1 ] + B

        

        dp_table = {}

        

        def helper( idx_a, idx_b ):

            

            if (idx_a, idx_b) in dp_table:

                return dp_table[(idx_a, idx_b)]

            

            

            if idx_a == 0 or idx_b == 0:

                # Any list compared to empty list give no uncrossed line

                return 0

            

            elif A[idx_a] == B[idx_b]:

                

                dp_table[(idx_a, idx_b)] = helper(idx_a-1, idx_b-1) + 1

                return dp_table[(idx_a, idx_b)]

            else:

                dp_table[(idx_a, idx_b)] = max( helper(idx_a-1, idx_b), helper(idx_a, idx_b-1))

                return dp_table[(idx_a, idx_b)]

        

        # --------------------------------------------

        return helper( len(A)-1, len(B)-1 )
