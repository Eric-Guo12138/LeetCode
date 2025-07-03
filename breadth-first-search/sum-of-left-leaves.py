# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 递归，若当前结点有左结点且该左结点没有左右孩子，则为左叶子结点，加到数组中
        res = []
        def dfs(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                res.append(root.left.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return sum(res)