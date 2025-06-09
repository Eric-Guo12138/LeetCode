class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 设置两个空列表ans0,ans1分别用来存储两个数组互相不在另一个数组的元素
        # 遍历nums1，如果元素不在nums2和ans0中，将该元素加到ans0，nums2同理
        # 最后返回ans0和ans1
        ans0,ans1 = [],[]
        for i in nums1:
            if i not in nums2 and i not in ans0:
                ans0.append(i)
        for j in nums2:
            if j not in nums1 and j not in ans1:
                ans1.append(j)
        return [ans0,ans1]