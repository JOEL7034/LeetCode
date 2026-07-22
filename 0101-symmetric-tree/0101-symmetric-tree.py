# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        # Base case: both nodes are None
        if not t1 and not t2:
            return True
        
        # Base case: one node is None and the other isn't
        if not t1 or not t2:
            return False
        
        # Values must match, and subtrees must be mirror images:
        # outer children (t1.left & t2.right) and inner children (t1.right & t2.left)
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)