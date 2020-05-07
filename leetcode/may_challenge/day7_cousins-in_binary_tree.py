'''
bfs soln
'''
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        if not root:
            return false
        
        stack = [[root, 0, -1]]
        
        cousin_1 = []
        cousin_2 = []
        
        while stack:
            node, h, parent = stack.pop()
            
            # find cousins
            if node.val == x: cousin_1 = [h, parent]
            if node.val == y: cousin_2 = [h, parent]
            
            if node.right: stack.append([node.right, h+1, node.val])
            if node.left: stack.append([node.left, h+1, node.val])
        
        if cousin_1[0] == cousin_2[0] and cousin_1[1] != cousin_2[1]:
            return True
        return False
'''
queue
'''
import queue
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dict_h= self.traverse(root,x,y)
        if x in dict_h and y in dict_h:
            h1= dict_h[x]['height']
            p1= dict_h[x]['parent']
            
            h2= dict_h[y]['height']
            p2= dict_h[y]['parent']
            
            if (h1==h2) and (p1!=p2):
                return True
        
        return False

     
    
    def traverse(self, node,c,d):
        q=[]
        q.append(node)
        
        height=0
        dict_h={}
        d={}
        d['height']=0
        d['parent']=None
        dict_h[node.val]=d
        height+=1
        while q:
            
            count=len(q)
            
            while count>0:
                dict_info={}
                l=[]
                x= q.pop(0)
                v= x.val
                l.append(v)
                dict_inf0={}
                if x.left !=None:
                    q.append(x.left)
                    dict_info['parent']=x.val
                    dict_info['height']=height
                    dict_h[x.left.val]=dict_info
                if x.right!=None:
                    q.append(x.right)
                    dict_info['parent']=x.val
                    dict_info['height']=height
                    dict_h[x.right.val]=dict_info

                
                count-=1
            height+=1
        return (dict_h)
            



'''
20 ms dfs soln
'''
class Solution(object):
    def isCousins(self, root, x, y):
       
        lookup = {} #dictionary for maintaining the level and value of the node
        def dfs(root, level=0, value=None):
            if root:
                if root.val in (x, y): 
                    lookup[root.val] = (level, value)
                dfs(root.left, level=level+1, value=root.val)
                dfs(root.right, level=level+1, value=root.val)
        dfs(root)
        return lookup[x][0] == lookup[y][0] and lookup[x][1] != lookup[y][1]



#class Solution:

'''
fast soln
'''
 def depth(root,x,par,level):
            if not root:
                return 
            
            if root.val==x:
                return [level,par]
            
            return depth(root.left,x,root,level+1) or depth(root.right,x,root,level+1)
        
        a=depth(root,x,None,1)
        b=depth(root,y,None,1)
        if a[0]==b[0] and a[1]!=b[1]:
            return True
        return False



'''
Fastest Python soln
'''

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        px = []
        py = []
        def checkTree(r,d):
            if r.left:
                if r.left.val == x:
                    px.append(r.val)
                    px.append(d+1)
                if r.left.val == y:
                    py.append(r.val)
                    py.append(d+1)
                checkTree(r.left,d+1)
            if r.right:
                if r.right.val == x:
                    px.append(r.val)
                    px.append(d+1)
                if r.right.val == y:
                    py.append(r.val)
                    py.append(d+1)
                checkTree(r.right,d+1)
        if root:
            if root.val == x or root.val == y:
                return False
            checkTree(root,1)
            print(px,py)
            if px[0]!=py[0] and px[1]==py[1]:
                return True
        return False   
