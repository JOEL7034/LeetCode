class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Check left subtree height
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            
            # Check right subtree height
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            # If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of the current subtree
            return max(left_height, right_height) + 1
        
        return check_height(root) != -1