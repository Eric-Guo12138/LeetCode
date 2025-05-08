class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 初始化字典，统计ransomNote中各字符数量，遇到+1，
        # 然后统计magazine中各字符数量，遇到-1
        # 遍历字典的值，若存在大于0，则说明ransomNote中字符有剩余，返回False
        dic = defaultdict(int)
        for c in ransomNote:
            dic[c] += 1
        for c in magazine:
            dic[c] -= 1
        for val in dic.values():
            if val > 0:
                return False
        return True