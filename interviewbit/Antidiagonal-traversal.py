class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        
        m=len(A)
        n=len(A[0])
        listy=[]
        for i in range(m+n-1):
            ni=[]
            for j in range(i+1):
                
                if(j>=m or i-j>=n):
                    continue;
                k=i-j;
                
                ni.append(A[j][k])
            listy.append(ni)
        return listy
'''
Input:  

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]

'''