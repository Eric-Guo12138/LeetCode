# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 根结点为空，返回0
        # 根结点非空，递归遍历左子树和右子树
        if root == None:
            return 0
        leftNodes = self.countNodes(root.left)
        rightNodes = self.countNodes(root.right)
        return (leftNodes + rightNodes + 1)