# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sum=0
        def dfs(node):
            if node==None:
                return False
            self.sum+=node.val
            if node.left==None and node.right==None and self.sum==targetSum:
                return True
            left=dfs(node.left)
            right=dfs(node.right)
            self.sum-=node.val
            return left or right
        return dfs(root)


            
        
        

          
        