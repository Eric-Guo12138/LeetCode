# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 分类比较
        # 根结点为空，真
        # 根结点不为空：左、右一个为空，假；左右都空，真；左、右都不为空：左！=右，假；左=右，再继续比较子树
        # 继续比较用到了递归
        if root is None:
            return True
        def compare(left,right):
            if left is None and right is not None:
                return False
            if right is None and left is not None:
                return False
            if left is None and right is None:
                return True
            if left.val != right.val:
                return False
            if left.val == right.val:
                return compare(left.left,right.right) and compare(left.right,right.left)
        return compare(root.left,root.right)