# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        if not root:
            return 0
        
        def dfs(root):
            nonlocal cnt, res
            if not root:
                return
            dfs(root.left)
            cnt -= 1
            if cnt == 0:
                res = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return res
        
