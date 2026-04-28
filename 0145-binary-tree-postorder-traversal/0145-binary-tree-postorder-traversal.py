# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def tran(node):
            if not node:
                return
            tran(node.left)
            tran(node.right)
            ans.append(node.val)
        tran(root)
        return ans