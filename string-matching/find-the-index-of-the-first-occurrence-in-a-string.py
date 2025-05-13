class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 枚举，在haystack中寻找等于needle的部分
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+n] == needle:
                return i
        return -1