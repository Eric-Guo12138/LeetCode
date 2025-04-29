class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
                nums1[m+i] = nums2[i]
        for i in range(n):
            for j in range(m):
                if nums1[m+i] < nums1[j]:
                    tem = nums1[j]
                    nums1[j] = nums1[m+i]
                    nums1[m+i] = tem
                