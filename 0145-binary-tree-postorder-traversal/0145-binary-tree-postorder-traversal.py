class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        res, stack, prev = [], [], None
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack[-1]
            
            if node.right and node.right is not prev:
                curr = node.right
            else:
                res.append(node.val)
                prev = stack.pop()

        return res