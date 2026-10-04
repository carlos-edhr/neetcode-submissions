# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []
        curr = root

        while curr or stack:
            # 1. Descend as far left as possible, remembering the path
            while curr:
                stack.append(curr)
                curr = curr.left
            # 2. The deepest pending ancestor is next in in-order 
            curr = stack.pop()
            result.append(curr.val)

            # 3. Its right subtree is the next region to visit
            curr = curr.right
        
        return result



        