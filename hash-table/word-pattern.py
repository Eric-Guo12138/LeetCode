class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 创建两个字典dic1,dic2
        # 将pattern对s的映射存放在dic1,s对pattern的映射存放在dic2
        # 返回True的条件是pattern的字母和s的单词可以互相映射
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        dic1,dic2 = dict(),dict()
        for i in range(len(pattern)):
            if (pattern[i] in dic1 and dic1[pattern[i]] != s[i]) or (s[i] in dic2 and dic2[s[i]] != pattern[i]):
                return False
            dic1[pattern[i]] = s[i]
            dic2[s[i]] = pattern[i]
        return True