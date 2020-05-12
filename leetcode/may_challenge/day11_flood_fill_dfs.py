'''
Fastest 60 ms
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        R, C = len(image), len(image[0])
        
        def is_safe(r, c):
            if r >= 0 and r < R and c >= 0 and c < C:
                return True
            else:
                return False
            
        visited = set()
        color = image[sr][sc]
        
        
        def dfs(sr, sc):
            if (sr, sc) in visited:
                return 
            
            visited.add((sr, sc))
            
            image[sr][sc] = newColor
            
            reach = [i for i in [(sr - 1, sc), (sr + 1, sc), (sr, sc + 1), (sr, sc - 1)] if is_safe(i[0], i[1])]        
            for each in reach:
                
                if image[each[0]][each[1]] == color:
                    
                    dfs(each[0], each[1])
        
        dfs(sr, sc)
        return image
        
'''
Second Fastest 64 ms
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if len(image) == 0:
            return []
        
        X, Y = len(image), len(image[0])
        color = image[sr][sc]
        
        if color == newColor:
            return image
        
        frontier_stack = [(sr, sc)]
        while len(frontier_stack) > 0:
            point = frontier_stack.pop()
            x, y = point[0], point[1]
            image[x][y] = newColor
            
            candidates = ((x + 1, y),
                          (x - 1, y),
                          (x, y + 1),
                          (x, y - 1),)
            for cand in candidates:
                x, y = cand[0], cand[1]
                if x >= X or x < 0 or y >= Y or y < 0:
                    continue
                if image[x][y] == color:
                    frontier_stack.append(cand)
        
        return image 
        
  '''
  68 ms
  '''
  def can_visit(row,column,image,visited):

    
    if row<0 or row>=len(image):
        return False
    if column<0 or column>=len(image[0]):
        return False
    if visited[row][column]:
        return False
    return True


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        
        def BFS(row,col,newColor,image):
            
            
            from collections import deque
            
            visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
            q = deque([])
            q.append((row,col))
            
            color = image[row][col]
            row_delta = [-1,0,0,1]
            col_delta = [0,-1,1,0]
            
            
            while q:
                row,col = q.pop()
                visited[row][col]=True
                image[row][col]=newColor
                
                for i in range(len(row_delta)):
                    newRow = row + row_delta[i]
                    newCol = col + col_delta[i]
                    
                    if can_visit(newRow,newCol,image,visited) and image[newRow][newCol]==color:
                        q.append((newRow,newCol))
                        
                        
        if not image:
            return
        
        BFS(sr,sc,newColor,image)
        
        return image
 
 '''
 Editorial
 '''
 class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #TC: O(n)
        #SC: O(n)
        #dfs_based editorial approach 
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
 
  '''
 78 ms
 '''
 class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return image
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        
        def dfs(i, j, ):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if image[i][j] != original_color:
                return
            if image[i][j] == newColor:
                return 
            image[i][j] = newColor
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)
        
        if original_color != newColor:
            dfs(sr, sc)
        return image
        
        
 '''
 Least Memory consuming
 '''
 class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if (image[sr][sc]==newColor):
            return image
        
        
        def adjacent_flood(sr,sc):
            adjacent  = (sr-1,sc),(sr+1,sc),(sr,sc-1),(sr,sc+1)
            for x,y in adjacent:
                if (x>=0) and (x<len(image)) and (y >=0) and (y<len(image[0]))and (image[x][y]== color):
                    image[x][y]= newColor
                    adjacent_flood(x,y)
        
        color = image[sr][sc]
        image[sr][sc] = newColor

        adjacent_flood(sr,sc)               
        
        return image     
