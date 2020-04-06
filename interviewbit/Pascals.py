'''
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
       res=[] 
       trow = [1]
       y = [0]
       for x in range(max(A,0)):
          res.append(trow)
          trow=[l+r for l,r in zip(trow+y, y+trow)]
       return res
