# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # Check if the node's value is within the allowed range
            if not (min_val < node.val < max_val):
                return False
            
            # Recursively check the left and right subtrees
            # For the left subtree, the node's value is the new max_val
            # For the right subtree, the node's value is the new min_val
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        # Start the validation with an infinite range
        return validate(root, float('-inf'), float('inf'))


        