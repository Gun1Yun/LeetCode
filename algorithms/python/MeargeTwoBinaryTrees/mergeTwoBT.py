"""
617. Merge Two Binary Trees (https://leetcode.com/problems/merge-two-binary-trees/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r1, r2):
            # add r1 tree to r2 tree
            if r1 is None:
                return
            r2.val += r1.val
            if r1.left is not None:
                if r2.left is None:
                    r2.left = TreeNode()
                dfs(r1.left, r2.left)
            if r1.right is not None:
                if r2.right is None:
                    r2.right = TreeNode()
                dfs(r1.right, r2.right)

        if root1 is None and root2 is None:
            return 
            
        result = TreeNode()
        dfs(root1, result)
        dfs(root2, result)
        return result

