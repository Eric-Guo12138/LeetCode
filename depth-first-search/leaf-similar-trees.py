# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 设置深度优先搜索的函数，用来存储叶子序列
        # 递归遍历，如果左右结点都为空，就加到序列里，否则递归左结点、右结点
        # 比较两棵二叉树的叶子序列，如果相同返回True
        result1 = []
        result2 = []
        self.dfs(root1,result1)
        self.dfs(root2,result2)
        return result1 == result2
    def dfs(self,root,result):
        if root is None:
            return 
        if root.left is None and root.right is None:
            result.append(root.val)
        self.dfs(root.left,result)
        self.dfs(root.right,result)