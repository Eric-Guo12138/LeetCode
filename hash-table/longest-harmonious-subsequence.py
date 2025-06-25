class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # 初始化一个字典，用来存放nums中每个元素和出现次数,初始化ans存放结果
        # 遍历nums，当前元素num次数加一，如果与该元素相差1的数也在字典中
        # 计算num和num-1或num+1出现次数的和，结果也就是ans和该和两个数中更大的一个
        cnts = defaultdict(int)
        ans = 0
        for num in nums:
            cnts[num] += 1
            if (num-1) in cnts:
                ans = max(ans,cnts[num]+cnts[num-1])
            if (num+1) in cnts:
                ans = max(ans,cnts[num]+cnts[num+1])
        return ans