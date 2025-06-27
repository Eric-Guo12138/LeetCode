class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 设置ans为返回值，cnt为数组中1的连续出现次数
        # 遍历数组，遇到值为0的把cnt重置为0，非0的cnt+1，返回和ans中更大的值
        ans = cnt = 0
        for num in nums:
            if x:
                cnt += 1
                ans = max(ans,max)
            else:
                cnt = 0
        return ans