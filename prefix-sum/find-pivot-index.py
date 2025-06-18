class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 设定初始左侧元素和sum_left、右侧元素和sum_right为0、sum(nums)
        # 遍历数组，sum_right先减去nums[i]
        # 如果此时sum_right == sum_left，i就是中心下标
        # 否则sum_left加上nums[i]，继续遍历
        sum_left,sum_right = 0,sum(nums)
        for i in range(len(nums)):
            sum_right -= nums[i]
            if sum_right == sum_left:
                return i
            sum_left += nums[i]
        return -1