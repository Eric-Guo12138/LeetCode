class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 设置两个空字典，分别用来存储数组中元素出现的频率和频率出现的次数
        # 如果频率出现次数>1，则说明存在重复频率，返回False,否则返回True
        dic,res = defaultdict(int),defaultdict(int)
        for num in arr:
            dic[num] += 1
        for value in dic.values():
            res[value] += 1
        for cnt in res.values():
            if cnt > 1:
                return False
        return True