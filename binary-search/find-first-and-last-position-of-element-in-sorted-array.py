class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        a = mid
        while a < len(nums) - 1:
            for b in range(a + 1,len(nums)):
                if nums[b] == target:
                    b += 1
        return [a,b]