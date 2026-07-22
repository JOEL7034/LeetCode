# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both nodes are None (trees match up to this point)
        if not p and not q:
            return True
        
        # Base case 2: One node is None and the other isn't (structures differ)
        if not p or not q:
            return False
        
        # Check current values and recursively check left and right subtrees
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)