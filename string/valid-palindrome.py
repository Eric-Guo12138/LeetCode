class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 将s的所有字母转换成小写，从后往前遍历s，如果有非字母数字字符，删除
        # 前后分别设置两个指针，如果s[i]!=s[j]，返回False,否则i+1,j-1,直到i>=j
        s = s.lower()
        m = len(s) - 1
        while m >= 0:
            if not s[m].isalnum():
                s = s.replace(s[m],'')
                m -= 1
            else:
                m -= 1
        i,j = 0,len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True