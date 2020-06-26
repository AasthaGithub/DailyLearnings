#mine 
class Solution:
    def __init__(self):
        self.sumy=0
    def dfs(self,root, thisSum):        
        if not root.left and not root.right:
            self.sumy+=thisSum            
        if root.left:
            self.dfs(root.left, thisSum*10+root.left.val)
        if root.right:
            self.dfs(root.right, thisSum*10+root.right.val)            
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0     
        self.dfs(root,root.val)
        return self.sumy
        
#fastest
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = [0]
        cr = [0]
        def traverse(node):
            if node.left is None and node.right is None:
                result[0] += cr[0]*10 + node.val
                return
            cr[0] = cr[0]*10 + node.val
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            cr[0] = cr[0]//10
        if root is not None:
            traverse(root)
        return result[0]
        
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        def df(root, num):
            if not root:
                return
            num = num*10+root.val
            if not root.left and not root.right:
                nonlocal ans
                ans += num
            else:
                df(root.left, num)
                df(root.right, num)

        df(root, 0)
        return ans        
