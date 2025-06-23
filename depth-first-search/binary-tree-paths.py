# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 如果当前结点是空，返回；如果是叶结点，把结点值加到path末尾
        # 如果不是叶结点，加上"->",再递归左结点和右结点
        ans = []
        def dfs(node,path):
            if node is None:
                return
            path += str(node.val)
            if node.left is None and node.right is None:
                ans.append(path)
            path += '->'
            dfs(node.left,path)
            dfs(node.right,path)
        dfs(root,"")
        return ans