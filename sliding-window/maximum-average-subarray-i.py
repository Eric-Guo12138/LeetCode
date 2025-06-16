class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 枚举数组，设定一个固定窗口用来统计窗口元素和，当元素个数超过窗口时，删去第一个元素
        max_s = -inf
        sum = 0
        for i,x in enumerate(nums):
            sum += x
            if i < k - 1:
                continue
            max_s = max(max_s,sum)
            sum -= nums[i-k+1]
        return max_s / k