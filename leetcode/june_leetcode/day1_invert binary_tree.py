# mine 32 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            
            if root.right and root.left:
                root.right,root.left=root.left,root.right
                self.invertTree( root.left )
                self.invertTree( root.right )
            
            elif not root.right:
                root.right=root.left
                root.left=None
                self.invertTree( root.right )
                
            elif not root.left:
                root.left=root.right
                root.right=None
                self.invertTree( root.left )   
            
            
            return root
        
        else:
            return  None
        
        
        
 #fastest 8 ms
 
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        
