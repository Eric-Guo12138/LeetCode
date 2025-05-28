class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 将s的所有字母转换成小写，遍历s，将所有字母数字字符保存到t中
        # 前后分别设置两个指针，如果t[i]!=t[j]，返回False,否则i+1,j-1,直到i>=j
        s = s.lower()
        t = []
        for i in s:
            if i.isalnum():
                t.append(i)
        i,j = 0,len(t)-1
        while i < j:
            if t[i] == t[j]:
                i += 1
                j -= 1
            else:
                return False
        return True