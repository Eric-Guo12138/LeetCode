class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 若两个字符串长度不等，返回False
        # 初始化字典，统计s中各字符数量，遇到+1，然后统计t中各字符数量，遇到-1
        # 遍历字典的值，若均为0，则返回True
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            dic[c] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True