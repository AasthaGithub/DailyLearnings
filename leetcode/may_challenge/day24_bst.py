#fastest 8 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        #1 recursive:
        """
        if not preorder:
            return None
        
        val = preorder[0]
        i = 1
        while i < len(preorder):
            if preorder[i] > val:
                break
            i += 1
            
        root = TreeNode(val)
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        
        return root
        """
        
        #1.5 refine
        return self.helper(preorder, 0, len(preorder) - 1)
    
    def helper(self, preorder, start, end):
        if start > end:
            return None
        
        idx = start + 1
        root = TreeNode(preorder[start])
        while idx <= end:
            if preorder[idx] > root.val:
                break
            idx += 1
            
        
        root.left = self.helper(preorder, start + 1, idx - 1)
        root.right = self.helper(preorder, idx, end)
        
        return root
        
        
        #2
        """
        return self.helper(preorder[::-1], float('-inf'), float('inf'))
    
    def helper(self, preorder, min_val, max_val):
        if preorder and min_val < preorder[-1] < max_val:
            root = TreeNode(preorder.pop())
            root.left = self.helper(preorder, min_val, root.val)
            root.right = self.helper(preorder, root.val, max_val)
            return root
        return None
        """












#12 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder_(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        for idx in range(1, len(preorder)):
            self.insertNode(root, TreeNode(preorder[idx]))
        return root
        
    def insertNode(self, parent, new_node):
        if new_node.val > parent.val:
            if not parent.right:
                parent.right = new_node
            else:
                self.insertNode(parent.right, new_node)
        if new_node.val <= parent.val:
            if not parent.left:
                parent.left = new_node
            else:
                self.insertNode(parent.left, new_node)
    
            
        
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """    
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        st = [root]
        
        for i in range(1, len(preorder)):
            if preorder[i] <= st[-1].val:
                new_node = TreeNode(preorder[i])
                st[-1].left = new_node
                st.append(new_node)
            else:
                while(len(st)>0 and st[-1].val < preorder[i]):
                    last_node = st.pop()
                new_node = TreeNode(preorder[i])
                last_node.right = new_node
                st.append(new_node)
        return root
