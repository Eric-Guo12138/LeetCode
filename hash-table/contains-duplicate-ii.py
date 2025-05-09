class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 初始化字典，枚举nums将元素和出现的位置放在字典里
        # 如果x在字典里并且i-dic[x]<=k，返回true
        dic = defaultdict(int)
        for i,x in enumerate(nums):
            if x in dic and i - dic[x] <= k:
                return True
            dic[x] = i
        return False