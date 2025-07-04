class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # 设置两个函数分别用来判断是否为单调增或单调减的数列，如果有一个为真则返回真
        return self.isIncreasing(nums) or self.isDecreasing(nums)

    def isIncreasing(self,nums):
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] < 0:
                return False
        return True

    def isDecreasing(self,nums):
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 0:
                return False
        return True