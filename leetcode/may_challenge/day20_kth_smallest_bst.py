'''
fastest 24 ms
'''

class Solution(object):
    def kthSmallest(self, root, k):
        queue = []
        while root:
            queue.append(root)
            root = root.left
        while k>1:
            k -= 1
            node = queue.pop()
            node = node.right
            while node:
                queue.append(node)
                node = node.left
        return queue[-1].val
        
#28 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(root):
            if root is not None:
                # check the left, may be None or val
                res = helper(root.left)
                
                if res is None:
                    
                    self.k -= 1
                    if self.k == 0:
                        return root.val
                    else:
                        return helper(root.right)
                
                else:
                    return res
            
            else:
                return
                
        self.k = k
        return helper(root)
        
        
  #40 ms
  
          a = []
        def small(root, k):
        
            if root == None:
                return

            small(root.left, k)
            a.append(root.val)
            if len(a) == k:
                return
            small(root.right, k)
        
        small(root, k)
        
        return a[k-1]
        
        
 # Binary search iterative
class Solution(object):
    def kthSmallest(self, root, k):
        count = self.get_nodes(root.left)
        while count + 1 != k:
            if count + 1 < k:
                root = root.right
                k = k - count - 1
            else:
                root = root.left
            count = self.get_nodes(root.left)
        return root.val

    def get_nodes(self, root):
        if not root:
            return 0
        return 1 + self.get_nodes(root.left) + self.get_nodes(root.right)


# Binary search recursive
class Solution_2(object):
    def kthSmallest(self, root, k):
        count = self.get_nodes(root.left)
        if count+1 < k:
            return self.kthSmallest(root.right, k-count-1)
        elif count+1 == k:
            return root.val
        else:
            return self.kthSmallest(root.left, k)

    def get_nodes(self, root):
        if not root:
            return 0
        return 1 + self.get_nodes(root.left) + self.get_nodes(root.right)


# DFS in-order iterative:
class Solution_3(object):
    def kthSmallest(self, root, k):
        node_stack = []
        count, result = 0, 0
        while root or node_stack:
            if root:
                node_stack.append(root)
                root = root.left
            else:
                if node_stack:
                    root = node_stack.pop()
                    result = root.val
                    count += 1
                    if count == k:
                        return result
                    root = root.right

        return -1   # never hit if k is valid


# DFS in-order recursive:
class Solution_4(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.num = 0
        self.in_order(root)
        return self.num

    def in_order(self, root):
        if root.left:
            self.in_order(root.left)
        self.k -= 1
        if self.k == 0:
            self.num = root.val
            return
        if root.right:
            self.in_order(root.right)


# DFS in-order recursive, Pythonic approach with generator:
class Solution_5(object):
    def kthSmallest(self, root, k):
        for val in self.in_order(root):
            if k == 1:
                return val
            else:
                k -= 1

    def in_order(self, root):
        if root:
            for val in self.in_order(root.left):
                yield val
            yield root.val
            for val in self.in_order(root.right):
                yield val       
