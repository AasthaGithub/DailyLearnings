#136 ms mine
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)    #rows
        if m==0:
            return
        
        n=len(board[0]) #cols
        
        def dfs(i,j,board):
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!="O":
                return 
            board[i][j]='#'
            dfs(i-1,j,board)
            dfs(i+1,j,board)
            dfs(i,j-1,board)
            dfs(i,j+1,board)
            
        for i in range(m): 
            if board[i][0]=='O':
                dfs(i,0,board)
            if board[i][n-1]=='O':
                dfs(i,n-1,board)     
            #for evry row make its starting & ending # if its 'O ' & travel its neighbors & make it 'o'
        
        for i in range(n): 
            #for every col
            if board[0][i]=='O': #For row 0
                dfs(0,i, board)
            if board[m-1][i]=='O': # For row m-1
                dfs(m-1,i,board)
        
        for i in range(m):       
            for j in range(n):
                if board[i][j]=='#':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
                    
                        
        return         
        
        
        
#fastest 124 ms

'''
130. Surrounded Regions     Medium

Given a 2D board containing 'X' and 'O' (the letter O),
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in
that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border,
which means that any 'O' on the border of the
board are not flipped to 'X'. Any 'O' that is
not on the border and it is not connected to
an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent
cells connected horizontally or vertically.

Accepted
207.5K
Submissions
784.3K
'''
from typing import Dict, List, Set

def extend_safety(grid: List[List[str]], row: int, col: int, safe: Set, seen: Set) -> None:
    '''
    Given a point next to a safe 0-point, check if it is also 0, in which
    case mark it safe and extend safety to its non-x neighbors.
    Explore RLTB (Right, Left, Top, Bottom).
    TODO: ? micro-optimize ?
    '''
    if (row, col) in seen:
        return
    seen.add((row, col))
    if grid[row][col] != 'X':
        safe.add((row, col))    # mark as safe first, then explore more
        if col + 1 < len(grid[row]):
            extend_safety(grid, row, col + 1, safe, seen)
        if col > 0:
            extend_safety(grid, row, col - 1, safe, seen)
        if row + 1 < len(grid):
            extend_safety(grid, row + 1, col, safe, seen)
        if row > 0:
            extend_safety(grid, row - 1, col, safe, seen)


def board_capture(board: List[List[str]]) -> None:
    '''
    Runtime: 144 ms, faster than 78.18% of Python3 online submissions for Surrounded Regions.
    Memory Usage: 15.4 MB, less than 49.64% of Python3 online submissions for Surrounded Regions.
    '''
    rows = len(board)
    if not rows:
        return
    cols = len(board[0])
    if not cols:
        return
    safe = set()
    seen = set()
    for row in [0, rows-1]:
        for col in range(cols):
            extend_safety(board, row, col, safe, seen)
    for col in [0, cols-1]:
        for row in range(1, rows-1):
            extend_safety(board, row, col, safe, seen)
    # print("SAFE:", safe)
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if (row, col) not in safe:
                board[row][col] = 'X'


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_capture(board)
        
        
#128 ms
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        boarders = [
            ij
            for k in range(max(m, n))
            for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))
        ]

        while boarders:
            i, j = boarders.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                boarders += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        for row in board:
            for i, cell in enumerate(row):
                if cell == 'S':
                    row[i] = 'O'
                else:
                    row[i] = 'X'
