class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找，计算区间[i,j]的中点m,如果nums[m]正好为target，返回m
        # 如果nums[m]<target，说明target在位置m右边，令区间左端点为m+1
        # 如果nums[m]>target，说明target在位置m左边，令区间右端点为m-1
        # 如果在i<=j内没找到，说明不存在target，返回-1
        i,j = 0,len(nums)-1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
        return -1