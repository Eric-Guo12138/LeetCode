class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 如果s和t长度不等，返回False
        # 设两个空字典分别记录s到t和t到s的映射，依次遍历如果发现映射不等的情况返回False
        if len(s) != len(t):
            return False
        dic1,dic2 = dict(),dict()
        for i in range(len(s)):
            if s[i] in dic1 and dic1[s[i]] != t[i]:
                return False
            if t[i] in dic2 and dic2[t[i]] != s[i]:
                return False
            dic1[s[i]] = t[i]
            dic2[t[i]] = s[i]
        return True