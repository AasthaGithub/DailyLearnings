'''
simple 820 ms
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix)>=2 and len(matrix[0])>=2:
            for i in range(1,len(matrix)):
                for j in range(1,len(matrix[0])):
                    if matrix[i][j]==1:
                        matrix[i][j]=min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])+1
        return sum([sum(i) for i in matrix])
        
'''
fastest        576ms
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] and matrix[i][j-1] and matrix[i-1][j-1]:
                    k=min(matrix[i-1][j],matrix[i][j-1])
                    matrix[i][j]=k+1 if matrix[i-k][j-k] else k
                    
        return sum(sum(row) for row in matrix)
        
'''
612 ms
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        for i in range(1, len(matrix)):
                for j in range(1, len(matrix[i])):
                        if matrix[i][j] == 0:
                                continue
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                        
        s = 0
        
        for i in matrix:
                s += sum(i)
                
        return s
