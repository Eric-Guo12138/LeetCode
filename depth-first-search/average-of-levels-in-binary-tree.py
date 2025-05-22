# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 使用双向队列存储每一层的节点，从队列中取出节点，并加入子节点
        # 计算每层节点和/节点数，保存到数组中
        ans = []
        queue = deque([root])
        while queue:
            s = 0 
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(s/l)
        return ans