# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 首先看根结点，p,q都空：True,p,q只有一个空：False,p!=q:False
        # p=q:再递归比较p,q的左孩子和右孩子，如果左孩子和右孩子都相等，True,否则False
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val != q.val:
            return False
        leftSame = self.isSameTree(p.left,q.left)
        rightSame = self.isSameTree(p.right,q.right)
        return (leftSame and rightSame)