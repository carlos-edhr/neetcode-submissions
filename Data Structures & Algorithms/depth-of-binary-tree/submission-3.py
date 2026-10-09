# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Iterative BFS solution
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth






















        # if not root:
        #     return 0

        # queue = deque([root])
        # depth = 0

        # while queue:
        #     depth += 1

        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return depth

        
        #Recursive solution
        # if not root:
        #     return 0
        
        # #depth of each subtree, computed independently
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)

        # # The deepest path goest through the taller
        # return 1 + max(left_depth, right_depth)
        