# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced_flag = True  # Renamed for clarity

        def dfs(node):
            nonlocal is_balanced_flag
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(left_height - right_height) > 1:
                is_balanced_flag = False

            return 1 + max(left_height, right_height)
        
        dfs(root)

        return is_balanced_flag
