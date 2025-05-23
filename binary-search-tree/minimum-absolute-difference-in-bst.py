# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 中序遍历二叉树，将数据都存储在数组中
        # 遍历数组，依次计算每两个相邻数据的差值，返回最小值
        nums = []
        def ord(root):
            if root is None:
                return
            ord(root.left)
            nums.append(root.val)
            ord(root.right)
        ord(root)
        ans = nums[1] - nums[0]
        for i in range(2,len(nums)):
            ans = min(ans,nums[i] - nums[i-1])
        return ans