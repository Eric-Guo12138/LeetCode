class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 使用字典统计nums中每个数字出现次数，遍历字典[1,n]范围，如果有数字没出现过，添加到res列表
        dic = defaultdict(int)
        n = len(nums)
        res = []
        for num in nums:
            if num <= n:
                dic[num] += 1
        for d in range(1,n+1):
            if dic[d] == 0:
                res.append(d)
        return res