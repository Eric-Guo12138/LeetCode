class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 暴力解法依次遍历的时间复杂度O(n),不符合题目要求，所以要用二分查找
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                 left = mid + 1
        if nums[mid] != target:
            mid += 1
        return mid