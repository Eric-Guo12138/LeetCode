class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = -1
        b = -1
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
        if nums[a + 1] != target:
                b = a
        else:
            for b in range(a,len(nums)):
                if nums[b] == target:
                    b += 1
        return [a,b]