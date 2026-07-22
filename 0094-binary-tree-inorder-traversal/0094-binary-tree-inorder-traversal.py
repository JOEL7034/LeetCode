class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        curr = root
        
        while curr:
            if curr.left is None:
              
                res.append(curr.val)
                curr = curr.right
            else:
                
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                
               
                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left
                else:
                    
                    predecessor.right = None
                    res.append(curr.val)
                    curr = curr.right
                    
        return res