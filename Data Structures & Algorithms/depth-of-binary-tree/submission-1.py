# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        #depth of each subtree, computed independently
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The deepest path goest through the taller
        return 1 + max(left_depth, right_depth)
        