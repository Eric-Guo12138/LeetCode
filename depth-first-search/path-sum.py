# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 如果树为空，返回 False
        # 如果当前节点为叶子节点，且叶子节点的值等于目标和减去之前节点的值，返回 True
        # 递归左子树和右子树
        if root == None:
            return False
        if root.left == None and root.right == None and root.val == targetSum:
            return True

        leftTree = self.hasPathSum(root.left, targetSum - root.val)
        rightTree = self.hasPathSum(root.right, targetSum - root.val)
        
        return leftTree or rightTree