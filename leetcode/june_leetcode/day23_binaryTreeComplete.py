# simple soln to complete binary tree

class Solution:     
    def find_depth(self, node):
        if not node:
            return 0
        return 1 + self.find_depth(node.left)
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ld = self.find_depth(root.left)
        rd = self.find_depth(root.right)
        if ld == rd:
            return 2**ld + self.countNodes(root.right)
        else:
            return 2**rd + self.countNodes(root.left)




#complex fastest
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
    
        if not root.left:
            return 1
        
        def probe(root, path):
            node = root
            for p in path:
                node = node.left if p == '0' else node.right
            return node != None
        
        def bp(num, d):
            p = bin(num)[2:]
            return (d-1-len(p))*'0'+p
        
        d = 1
        node = root
        while node.left:
            node = node.left
            d += 1
        
        l, r = 0, 2**(d-1)-1
        while l < r:
            p = (l+r)//2
            if not probe(root, bp(p, d)):
                r = p-1
            else:
                l = p+1
        if probe(root, bp(r, d)):
            return r+2**(d-1)
        else:
            return r+2**(d-1)-1
