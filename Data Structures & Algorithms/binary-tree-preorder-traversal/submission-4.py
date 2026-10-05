# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result














        # if not root:
        #     return []


        # result = []
        # stack = [root]


        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)

        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        
        # return result

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
        # if not root:
        #     return []
        
        # result: List[int] = []

        # stack: List[TreeNode] = [root]

        # while stack:
        #     node = stack.pop()
        #     # visit before the children
        #     result.append(node.val)
            
        #     #push right first so the left child is popped firsst (LIFO)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
                
        # return result
            
        