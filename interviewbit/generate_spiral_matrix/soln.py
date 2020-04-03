class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        grid = [[0] * A for _ in range(A)]
        L = 0
        R = A - 1
        T = 0
        B = A - 1
        direction = 0
        num = 1
        
        while L <= R and T <= B:
            if direction == 0:
                for i in range(L, R + 1):
                    grid[T][i] = num
                    num += 1
                T += 1
            
            elif direction == 1:
                for i in range(T, B + 1):
                    grid[i][R] = num
                    num += 1
                R -= 1
            
            elif direction == 2:
                for i in range(R, L - 1, -1):
                    grid[B][i] = num
                    num += 1
                B -= 1
                
            elif direction == 3:
                for i in range(B, T-1, -1):
                    grid[i][L] = num
                    num += 1
                L += 1
            
            direction = (direction + 1) % 4
            
        return grid