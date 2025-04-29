class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从后往前填充，初始化三个指针，p指向合并后数组的末尾，p1,p2分别指向nums1和nums2末尾
        # 比较nums1[p1]、nums2[p2]的大小，较大的放到nums1[p]
        # 最后如果nums1还有元素不用管，nums2还有元素要合并到nums1
        p = m + n -1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
        if p1 < 0:
            while p2 >= 0:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1