class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 设置两个指针分别指向s,t的首字符
        # 如果s[i] == t[j]，i++,j++;s[i] != t[j],j++,直到遍历完s,t
        # 如果最后i正好为s长度，说明s中的字符都匹配成功，返回True
        i,j = 0,0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s):
            return True
        else:
            return False
